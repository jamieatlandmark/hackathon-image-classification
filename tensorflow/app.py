#!flask/bin/python
import tensorflow as tf
import sys
import os
from flask import Flask, request, redirect, url_for, jsonify, render_template
from werkzeug.utils import secure_filename
#app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')


UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print "fiel recveied"
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_path = UPLOAD_FOLDER + '/' + filename
            image_data = tf.gfile.FastGFile(image_path, 'rb').read()
            label_lines = [line.rstrip() for line
                               in tf.gfile.GFile("retrained_labels.txt")]
            # Unpersists graph from file
            with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(f.read())
                _ = tf.import_graph_def(graph_def, name='')
            with tf.Session() as sess:
                # Feed the image_data as input to the graph and get first prediction
                softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
                predictions = sess.run(softmax_tensor, \
                         {'DecodeJpeg/contents:0': image_data})
                # Sort to show labels of first prediction in order of confidence
                top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
                a = {}
                for node_id in top_k:
                    human_string = label_lines[node_id]
                    score = predictions[0][node_id]
                    a.update({human_string: float(score)})
                    #eturn('%s (score = %.5f)' % (human_string, score))
                    #return jsonify({'Result:': human_string,'Score:': score})
                print a
                return jsonify({'results': a, 'imgsrc':image_path})
                #return render_template('results.html', results=a, imgsrc=image_path)
    #return '''
    return render_template('dropzone.html')
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method=post enctype=multipart/form-data>
    #   <p><input type=file name=file>
    #      <input type=submit value=Upload>
    # </form>
    # '''


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

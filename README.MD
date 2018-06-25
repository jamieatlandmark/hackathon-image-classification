# Landmark Hackathon 2018 - Image Classification
## Tensorflow
- Ensure you have Docker installed and running on your local machine.
- Run the image - it will be pulled from dockerhub if this is the first time.
- `docker run -d -p 5000:5000 latitudehopper/tensor`
- Open up the GUI in your browser http://localhost:5000
- Drag sample images into the dropzone
- Check the results
#### Sources
- https://github.com/xblaster/tensor-guess
- https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/index.html

## Custom Vision Service
### OSGB Example
- Open the `index.html` file in your browser. (or use https://lighackathon.blob.core.windows.net/azure-customvision/index.html)
- This is a GUI to send image files to the Azure Custom Vision Service endpoint 
### Your Turn! - What's that flower?
- Download some sample images M:\Temporary Sharing Area\Hackathon\Dunbar\customvision-flowers.zip (218MB)
- Within the ZIP files are images of 4 species of flower
    - Daisy (633 images)
    - Dandelion (898 images)
    - Roses (641 images)
    - Sunflowers (699 images)
    - Tulips (799 images)
- Extract the files to your desktop
- Log in to Azure Custom Image service https://www.customvision.ai/

#### Sources
- Azure Custom Vision Service https://azure.microsoft.com/en-gb/services/cognitive-services/custom-vision-service/
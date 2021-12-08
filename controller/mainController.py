from controller import filterController, imagesController
import cv2

"""
This is the main controller of the program.
This is the controller that will be used to control the program.
"""

# Get all the images from the folder
images = imagesController.get_images()

for (i, image) in enumerate(images):
    dilate_image = filterController.to_dilate(image, 10)
    imagesController.write_images(dilate_image, image.replace('.jpg', '_dilate.jpg'))
    print("[INFO] processed image to dilate {}/{}".format(i + 1, len(images)))

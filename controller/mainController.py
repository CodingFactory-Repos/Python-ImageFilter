from controller import filterController, getImagesController
import cv2

"""
This is the main controller of the program.
This is the controller that will be used to control the program.
"""

# Get all the images from the folder
images = getImagesController.get_images()

print("Images: ", images)

for (i, image) in enumerate(images):
    gray_image = filterController.to_grayscale(image)
    cv2.imwrite(image.replace("images", "output"), gray_image)
    print("[INFO] processed image {}/{}".format(i + 1, len(images)))

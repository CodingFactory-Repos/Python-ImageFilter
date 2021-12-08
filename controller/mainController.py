from controller import filterController, getImagesController
import cv2

"""
This is the main controller of the program.
This is the controller that will be used to control the program.
"""

# Get all the images from the folder
images = getImagesController.get_images()

for (i, image) in enumerate(images):
    gray_image = filterController.to_grayscale(image)
    cv2.imwrite(image.replace("images", "output"), gray_image)
    print("[INFO] processed image to grayscale {}/{}".format(i + 1, len(images)))


for (i, image) in enumerate(images):
    blur_image = filterController.to_blur(image, 3)
    cv2.imwrite(image.replace("images", "output"), blur_image)
    print("[INFO] processed image to blur {}/{}".format(i + 1, len(images)))


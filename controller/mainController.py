import cv2

from controller import filterController, imagesController, argsController

"""
This is the main controller of the program.
This is the controller that will be used to control the program.
"""

args = ["-f", "--filter"]
images_list = imagesController.get_images()

for arg in args:
    if arg in argsController.get_args():
        filters_list = argsController.get_dictionary('--filter')

        for (i, image_path) in enumerate(images_list):

            image = cv2.imread(image_path)

            if filters_list['blur'] != None:
                image = filterController.to_blur(image, int(filters_list['blur']))
                print("[INFO] Blur filter applied")

            if filters_list['grayscale'] != None:
                image = filterController.to_grayscale(image)
                print("[INFO] Grayscale filter applied")

            if filters_list['dilate'] != None:
                image = filterController.to_dilate(image, int(filters_list['dilate']))
                print("[INFO] Dilate filter applied")

            imagesController.write_images(image, image_path)

            # dilate_image = filterController.to_dilate(image, 10)
            # imagesController.write_images(dilate_image, image.replace('.jpg', '_dilate.jpg'))
            # print("[INFO] processed image to dilate {}/{}".format(i + 1, len(images_list)))

# Get all the images from the folder

# if args[1] == "--filter":
#     if args[2].find("blur") != -1:
#         level = args[2].split("blur:")[1].split("|")[0]
#
#         # Blur the images
#         images = filterController.to_blur(images, level)
#
#     elif args[2].find("grayscale") != -1:
#         # Convert the images to grayscale
#         images = filterController.to_grayscale(images)
#
#     elif args[2].find("dilate") != -1:
#         level = args[2].split("dilate:")[1].split("|")[0]
#         # Dilate the images
#         images = filterController.to_dilate(images)

# for (i, image) in enumerate(images):
#     dilate_image = filterController.to_dilate(image, 10)
#     imagesController.write_images(dilate_image, image.replace('.jpg', '_dilate.jpg'))
#     print("[INFO] processed image to dilate {}/{}".format(i + 1, len(images)))

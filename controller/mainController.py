import cv2
from controller import filterController, imagesController, argsController, loggerController

"""
This is the main controller of the program.
This is the controller that will be used to control the program.
"""

loggerController.add_log("------ Program as been lunch ------")

args = ["-f", "--filter"]
images_list = imagesController.get_images()

for arg in args:
    if arg in argsController.get_args():
        if arg == "-f" or arg == "--filter":
            filters_list = argsController.get_dictionary(arg)

            loggerController.add_log(f"[Parameters] Filter : {str(filters_list)}\n")

            for (i, image_path) in enumerate(images_list):

                image = cv2.imread(image_path)

                loggerController.add_log(f"[Processing] Image {image_path} ({i + 1} of {len(images_list)})")

                if 'blur' in filters_list and filters_list['blur'] != None:
                    image = filterController.to_blur(image, filters_list['blur'])

                if 'grayscale' in filters_list and filters_list['grayscale'] != None:
                    image = filterController.to_grayscale(image)

                if 'dilate' in filters_list and filters_list['dilate'] != None:
                    image = filterController.to_dilate(image, filters_list['dilate'])

                loggerController.add_log(f"[Processing] Image {i + 1} of {len(images_list)} has been processed")
                imagesController.write_images(image, image_path)
                loggerController.add_log(f"[Processing] Image {i + 1} of {len(images_list)} has been saved (path: {image_path.replace('images', 'output')})\n")
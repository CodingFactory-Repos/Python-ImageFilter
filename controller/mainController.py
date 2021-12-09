import cv2
from controller import filterController, imagesController, argsController, loggerController

"""
This is the main controller of the program.
This is the controller that will be used to control the program.
"""

args = ["-f", "--filter"]
images_list = imagesController.get_images()
loggerController.add_log("------ Program as been lunch ------")
for arg in args:
    if arg in argsController.get_args():
        filters_list = argsController.get_dictionary('--filter')

        for (i, image_path) in enumerate(images_list):

            image = cv2.imread(image_path)

            print(f"-- --- --\n")
            print(f"Processing image {i+1} of {len(images_list)}")

            if 'blur' in filters_list and filters_list['blur'] != None:
                image = filterController.to_blur(image, filters_list['blur'], image_path)
                print("[INFO] Blur filter applied")

            if 'grayscale' in filters_list and filters_list['grayscale'] != None:
                image = filterController.to_grayscale(image, image_path)
                print("[INFO] Grayscale filter applied")

            if 'dilate' in filters_list and filters_list['dilate'] != None:
                image = filterController.to_dilate(image, filters_list['dilate'], image_path)
                print("[INFO] Dilate filter applied")

            print(f"[INFO] Saving image {images_list[i]}")
            imagesController.write_images(image, image_path)
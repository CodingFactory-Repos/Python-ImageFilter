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

            print(f"-- --- --\n")
            print(f"Processing image {i+1} of {len(images_list)}")

            if 'blur' in filters_list and filters_list['blur'] != None:
                image = filterController.to_blur(image, int(filters_list['blur']))
                print("[INFO] Blur filter applied")

            if 'grayscale' in filters_list and filters_list['grayscale'] != None:
                image = filterController.to_grayscale(image)
                print("[INFO] Grayscale filter applied")

            if 'dilate' in filters_list and filters_list['dilate'] != None:
                image = filterController.to_dilate(image, int(filters_list['dilate']))
                print("[INFO] Dilate filter applied")

            print(f"[INFO] Saving image {images_list[i]}")
            imagesController.write_images(image, image_path)
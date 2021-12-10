import os
import cv2
from controller import loggerController, iniController

"""
This controller is used to get all the images from the data folder.
"""


def get_images(actual_images=None):
    """
    Get all images from the data/images folder
    :param actual_images: list of images to be returned
    :return: list of images
    """
    if actual_images is None: # if no images are passed
        all_images = os.listdir(iniController.get_input_path()) # get all images from the data/images folder
    else: # if images are passed
        all_images = actual_images # get the images passed

    for (i, image) in enumerate(all_images):
        image_extension = image.split('.')[1] # get the extension of the image
        valid_images = ["jpg", "png", "tga", "jpeg"] # list of valid images

        if image_extension not in valid_images:  # if the extension is not valid
            all_images.remove(image) # remove the image from the list
            loggerController.add_log("[FileScan] Removed file: " + image) # add a log
            return get_images(all_images) # get the images again

    all_images = get_images_path(all_images) # get the path of the images

    return all_images # return the images


def get_images_path(images):
    """
    Get the path of the images
    :param images: get images
    :return: path of the images
    """
    for (i, image) in enumerate(images):
        images[i] = f"{iniController.get_input_path()}/{image}" # get the path of the images

    return images # return the images


def write_images(image, path):
    """
    Write all images to the data/output directory
    """

    cv2.imwrite(path.replace(iniController.get_input_path(), iniController.get_output_path()), image) # write the image to the output folder

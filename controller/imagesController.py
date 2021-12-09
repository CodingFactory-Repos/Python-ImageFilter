import os
import cv2
from controller import loggerController, iniController

"""
This controller is used to get all the myimages from the data folder.
"""


def get_images(actual_images=None):
    """
    Get all myimages from the data/myimages folder
    :param actual_images: list of myimages to be returned
    :return: list of myimages
    """
    if actual_images is None: # if no myimages are passed
        all_images = os.listdir(iniController.get_input_path()) # get all myimages from the data/myimages folder
    else: # if myimages are passed
        all_images = actual_images # get the myimages passed

    for (i, image) in enumerate(all_images):
        image_extension = image.split('.')[1] # get the extension of the image
        valid_images = ["jpg", "png", "tga", "jpeg"] # list of valid myimages

        if image_extension not in valid_images:  # if the extension is not valid
            all_images.remove(image) # remove the image from the list
            loggerController.add_log("[FileScan] Removed file: " + image) # add a log
            return get_images(all_images) # get the myimages again

    all_images = get_images_path(all_images) # get the path of the myimages

    return all_images # return the myimages


def get_images_path(images):
    """
    Get the path of the myimages
    :param images: get myimages
    :return: path of the myimages
    """
    for (i, image) in enumerate(images):
        images[i] = f"{iniController.get_input_path()}/{image}" # get the path of the myimages

    return images # return the myimages


def write_images(image, path):
    """
    Write all myimages to the data/output directory
    """

    cv2.imwrite(path.replace(iniController.get_input_path(), iniController.get_output_path()), image) # write the image to the output folder

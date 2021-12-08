import os
import cv2

"""
This controller is used to get all the images from the data folder.
"""


def get_images(actual_images=None):
    """
    Get all images from the data/images folder
    :param actual_images: list of images to be returned
    :return: list of images
    """
    if actual_images is None:
        all_images = os.listdir("./data/images")
    else:
        all_images = actual_images

    for (i, image) in enumerate(all_images):
        image_extension = image.split('.')[1]
        valid_images = ["jpg", "png", "tga", "jpeg"]

        if image_extension not in valid_images:
            all_images.remove(image)
            print("Removed: " + image)
            print("actual_images: " + str(all_images))
            print("-- --- --")
            return get_images(all_images)

    all_images = get_images_path(all_images)

    return all_images


def get_images_path(images):
    """
    Get the path of the images
    :param images: get images
    :return: path of the images
    """
    for (i, image) in enumerate(images):
        images[i] = "./data/images/" + image

    return images


def write_images(image, path):
    """
    Write all images to the data/output directory
    """
    cv2.imwrite(path.replace("images", "output"), image)

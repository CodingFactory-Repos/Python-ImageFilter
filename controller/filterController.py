import cv2
import numpy
from controller import loggerController

"""
This class is used to filter the image.
"""


def to_grayscale(image, image_path):
    """
    Convert a colored image to grayscale.
    :param path: path to the image
    :return: grayscale image
    """
    # Convert the image to grayscale.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    loggerController.add_log(f'Set image to grayscale: {image_path}')
    return gray


def to_blur(image, value, image_path):
    """
    Blur the image.
    :param path: path to the image
    :param value: value of the blur
    :return: blurred image
    """
    # Blur the image.
    value = value * 10
    blur = cv2.blur(image, (value, value))
    loggerController.add_log(f'Set image to blur: {image_path}')
    return blur


def to_dilate(image, value, image_path):
    """
    Dilate the image.
    :param path: path to the image
    :param value: value of the dilate
    :return: dilated image
    """
    # Dilate the image.
    kernel = numpy.ones((value, value), numpy.uint8) # Create a kernel.
    dilate = cv2.dilate(image, kernel) # Dilate the image.
    loggerController.add_log(f'Set image to dilate: {image_path}')
    return dilate
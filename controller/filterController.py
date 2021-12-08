import cv2
import numpy

"""
This class is used to filter the image.
"""


def to_grayscale(path):
    """
    Convert a colored image to grayscale.
    :param path: path to the image
    :return: grayscale image
    """
    # Convert the image to grayscale.
    img_path = cv2.imread(path)
    gray = cv2.cvtColor(img_path, cv2.COLOR_BGR2GRAY)
    return gray


def to_blur(path, value):
    """
    Blur the image.
    :param path: path to the image
    :param value: value of the blur
    :return: blurred image
    """
    # Blur the image.
    value = value * 10
    img_path = cv2.imread(path)
    blur = cv2.blur(img_path, (value, value))
    return blur


def to_dilate(path, value):
    """
    Dilate the image.
    :param path: path to the image
    :param value: value of the dilate
    :return: dilated image
    """
    # Dilate the image.
    img_path = cv2.imread(path)
    kernel = numpy.ones((value, value), numpy.uint8) # Create a kernel.
    dilate = cv2.dilate(img_path, kernel) # Dilate the image.
    return dilate
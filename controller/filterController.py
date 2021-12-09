import cv2
import numpy
from controller import loggerController

"""
This class is used to filter the image.
"""


def get_filters_available():
    """
    Get the available filters.
    :return: list of filters
    """
    # TODO: add more filters

    return ['grayscale', 'blur', 'dilate', 'text'] # Show the available filters

def to_grayscale(image, value):
    """
    Convert a colored image to grayscale.
    :param path: path to the image
    :return: grayscale image
    """
    # Convert the image to grayscale.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale.
    loggerController.add_log(f'[Filter] Grayscale filter applied') # Log the filter.

    return gray # Return the grayscale image.


def to_blur(image, value):
    """
    Blur the image.
    :param path: path to the image
    :param value: value of the blur
    :return: blurred image
    """
    # Blur the image.
    value = value * 10 # Convert the value to a multiple of 10.
    blur = cv2.blur(image, (value, value)) # Blur the image.
    loggerController.add_log(f'[Filter] Blur filter applied') # Log the filter.

    return blur # Return the blurred image.


def to_dilate(image, value):
    """
    Dilate the image.
    :param path: path to the image
    :param value: value of the dilate
    :return: dilated image
    """
    # Dilate the image.
    kernel = numpy.ones((value, value), numpy.uint8)  # Create a kernel.
    dilate = cv2.dilate(image, kernel)  # Dilate the image.
    loggerController.add_log(f'[Filter] Dilate filter applied') # Log the filter.

    return dilate # Return the dilated image.


def to_text(image, value):
    font = cv2.FONT_HERSHEY_SIMPLEX

    position = ((int) (image.shape[1]/2 - 268/2), (int) (image.shape[0]/2 - 36/2))

    text = cv2.putText(image, value, position, font, 1, (255, 255, 255), 2)
    loggerController.add_log(f'[Filter] Text filter applied') # Log the filter.

    return text
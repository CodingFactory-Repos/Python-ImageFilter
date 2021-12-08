import cv2

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

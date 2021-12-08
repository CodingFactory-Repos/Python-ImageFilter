import cv2
"""
This is the main controller of the program.
This is the controller that will be used to control the program.
"""

def to_grayscale(path):
    """
    This function will convert the image to grayscale.
    :param path: The image that will be converted to grayscale.
    :return: The grayscale image.
    """
    # Convert the image to grayscale.
    img_path = cv2.imread(path)
    gray = cv2.cvtColor(img_path, cv2.COLOR_BGR2GRAY)
    return gray
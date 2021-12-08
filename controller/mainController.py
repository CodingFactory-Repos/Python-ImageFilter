import cv2
"""
This is the main controller of the program.
This is the controller that will be used to control the program.
"""

image = cv2.imread('./data/images/dubai.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', image)
cv2.imshow('Gray image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
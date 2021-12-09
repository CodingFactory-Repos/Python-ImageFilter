from controller import mainController  # Import the main controller in controller/mainController.py
"""
Main file of the project.
This file is the entry point of the project.
There is no need to modify this file.
"""

try:
    mainController()  # Start the main controller
except Exception as e:
    print(e)
    print("An error has occurred. Please check the logs.")
    exit(1)
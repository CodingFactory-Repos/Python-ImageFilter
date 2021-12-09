from controller import iniController, mainController, loggerController  # Import the main controller in controller/mainController.py
"""
Main file of the project.
This file is the entry point of the project.
There is no need to modify this file.
"""

try:
    iniController()
    mainController()  # Start the main controller
except Exception as e:
    loggerController.add_log("[Error] An error occurred while running the main controller.")
    loggerController.add_log(f"The error is: {e}")
    loggerController.add_log("Exiting the program.")
    print(e)
    print("An error has occurred. Please check the logs.")
    loggerController.exit_application();
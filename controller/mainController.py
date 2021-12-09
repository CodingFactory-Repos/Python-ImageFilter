import cv2
from controller import filterController, imagesController, argsController, loggerController, iniController

"""
This is the main controller of the program.
This is the controller that will be used to control the program.
"""

loggerController.add_log("------ Program as been lunch ------")  # Add a program starting log to the log file

args = ["-f", "--filter"]  # List of arguments that can be used
images_list = imagesController.get_images()  # Get the list of myimages

for arg in args:  # For each autorized argument
    if arg in argsController.get_args():  # If the argument is in the list of arguments
        if arg == "-f" or arg == "--filter":  # If the argument is the filter
            filters_list = argsController.get_dictionary(arg)  # Get the list of filters
            filters_available_list = filterController.get_filters_available()  # Get the list of filters available

            loggerController.add_log(f"[Parameters] Filter : {str(filters_list)}\n")  # Add a log to the log file

            for (i, image_path) in enumerate(images_list):

                image = cv2.imread(image_path)  # Get the image pixels array
                loggerController.add_log(f"[Processing] Image {image_path} ({i + 1} of {len(images_list)})")  # Add a processing log to the log file

                for filters_available in filters_available_list:  # For each filter available
                    if filters_available in filters_list and filters_list[filters_available] is not None:  # If the filter is in the list of filters and the filter is not None
                        image = eval(
                            f"filterController.to_{filters_available}(image, filters_list['{filters_available}'])")  # Apply the filter to the image

                loggerController.add_log(
                    f"[Processing] Image {i + 1} of {len(images_list)} has been processed")  # Add a processing log to the log file
                imagesController.write_images(image, image_path) # Write the image to the output directory
                loggerController.add_log(f"[Processing] Image {i + 1} of {len(images_list)} has been saved (path: {image_path.replace(iniController.get_input_path(), iniController.get_output_path())})\n") # Add a processing log to the log file

print("Files have been saved in the output folder") # Print a end of program message
loggerController.add_log("------ Program has been finished ------") # Add a program ending log to the log file

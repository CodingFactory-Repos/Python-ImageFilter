import sys
from controller import configController


def get_args():
    """
    Get the arguments from the command line
    :return: list of arguments
    """
    if len(sys.argv) > 1:
        return sys.argv # main.py --filter "blur:2"
    else:
        return configController.get_ini() # --filter grayscale|blur:3|dilate:3

def get_params(argument):
    """
    Get the parameters from the command line
    :param argument: argument from the command line
    :return: parameters
    """
    parms_index = get_args().index(argument) + 1 # Get the index of the parameters
    parms = get_args()[parms_index] # Get the parameters
    return parms # Return the parameters


def get_dictionary(argument):
    """
    Get the dictionary from the command line
    :param argument: argument from the command line
    :return: dictionary
    """
    params = get_params(argument).split('|') # Get the parameters
    params_dict = {} # Create a dictionary

    for param in params:
        param = param.split(':') # Split the parameters

        if len(param) == 2: # If the parameter has a value
            try:
                params_dict[param[0]] = int(param[1]) # Add the parameter to the dictionary
            except ValueError:
                params_dict[param[0]] = param[1] # Add the parameter to the dictionary
        else: # If the parameter has no value
            if(param[0] == 'grayscale'): # If the parameter is grayscale
                params_dict[param[0]] = 0 # Add the parameter to the dictionary
            else: # If the parameter is not grayscale
                params_dict['getimages'] = param[0] # Add the parameter to the dictionary

    return params_dict # Return the dictionary
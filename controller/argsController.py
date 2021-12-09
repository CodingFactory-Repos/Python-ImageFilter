import sys


def get_args():
    """
    Get the arguments from the command line
    :return: list of arguments
    """
    return sys.argv


def get_params(argument):
    """
    Get the parameters from the command line
    :param argument: argument from the command line
    :return: parameters
    """
    parms_index = get_args().index(argument) + 1
    parms = get_args()[parms_index]
    return parms


def get_dictionary(argument):
    """
    Get the dictionary from the command line
    :param argument: argument from the command line
    :return: dictionary
    """
    params = get_params(argument).split('|')
    params_dict = {}

    for param in params:
        param = param.split(':')

        if len(param) == 2:
            params_dict[param[0]] = int(param[1])
        else:
            if(param[0] == 'grayscale'):
                params_dict[param[0]] = 0
            else:
                params_dict[param[0]] = None

    print(params_dict)
    return params_dict

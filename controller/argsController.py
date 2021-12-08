import sys


def get_args():
    return sys.argv


def get_params(argument):
    parms_index = get_args().index(argument) + 1
    parms = get_args()[parms_index]
    return parms


def get_dictionary(argument):
    params = get_params(argument).split('|')
    params_dict = {}

    for param in params:
        param = param.split(':')

        if len(param) == 2:
            params_dict[param[0]] = param[1]
        else:
            if(param[0] == 'grayscale'):
                params_dict[param[0]] = 0
            else:
                params_dict[param[0]] = None

    return params_dict

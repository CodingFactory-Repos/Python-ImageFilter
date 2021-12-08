from model import nameModel # import the model/nameModel.py

user_name = nameModel.name("John Doe") # Create a name object

def get_name_of_user():
    """
    Ask the user for their name, save it to the name object, and return it.
    :return: user_name
    """
    name = input("What is your name?\n> ")
    user_name.set_name(name)
    return user_name.get_name()
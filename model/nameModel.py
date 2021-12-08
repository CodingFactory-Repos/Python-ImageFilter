class name:
    """
    This class is used to create a name object.
    """
    def __init__(self, name): # Constructor
        """
        This is the constructor of the class.
        :param name: set the name of the object.
        """
        self.name = name

    def get_name(self): # Getter
        """
        This method is used to get the name of the object.
        :return: the name of the object.
        """
        return self.name

    def set_name(self, name): # Setter
        """
        This method is used to set the name of the object.
        :param name: set the new name of the object.
        """
        self.name = name
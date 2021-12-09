class ini:
    output_path = ""
    input_path = ""

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def get_output_path(self):
        return self.output_path

    def get_input_path(self):
        return self.input_path

    def set_output_path(self, output_path):
        self.output_path = output_path

    def set_input_path(self, input_path):
        self.input_path = input_path
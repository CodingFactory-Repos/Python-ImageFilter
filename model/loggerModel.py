class logger:
    log_file_path = ""

    def __init__(self, path):
        self.log_file_path = path

    def get_log_path(self):
        return self.log_file_path

    def set_log_path(self, path):
        self.log_file_path = path
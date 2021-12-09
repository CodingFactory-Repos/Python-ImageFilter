from datetime import datetime

"""
This class is responsible for logging the data from the sensors.
"""

log_file = "./data/logger.log" # Log file path


def add_log(message):
    """
    This function adds a log message to the log file.
    :param message:
    :return:
    """
    now = datetime.now() # Get current date and time
    timestamp = now.strftime('%Y/%m/%d %Hh %Mm %Ss') # Format date and time
    formatted = f'{timestamp} - {message}' # Format message

    print(formatted) # Print message to console
    with open(log_file, 'a') as f: # Open log file
        f.write(formatted + '\n') # Write message to log file


def dump_log():
    """
    This function dumps the log file to the console.
    :return:
    """
    with open(log_file, 'r') as f: # Open log file
        print(f.read()) # Print log file to console

def exit_application():
    """
    This function exits the application.
    :return:
    """
    print("Exiting application...")
    exit()
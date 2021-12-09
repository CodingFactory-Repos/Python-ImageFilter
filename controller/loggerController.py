from datetime import datetime
log_file = "./data/ImageFilter.log"


def add_log(message):
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    formatted = f'{timestamp} - {message}'
    with open(log_file, 'a') as f:
        f.write(formatted+ '\n')



def dump_log():
    with open (log_file,'r') as f:
        print(f.read())
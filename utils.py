import string
import datetime
import random


# generate random name for file
def file_name_generator(size, error_file, chars=string.ascii_uppercase + string.digits):
    now = datetime.datetime.now()
    time_str = "%s" % (now.strftime("%Y_%m_%d_%H_%M_%S"))
    if error_file:
        return "./logs/reconsciliation_" + time_str + "__Failed__" + ''.join(random.choice(chars) for _ in range(size))

    if not error_file:
        return "./logs/reconsciliation_" + time_str + "__Success__" + ''.join(random.choice(chars) for _ in range(size))


def generate_log_file(file_name):
    return open(file_name, 'w')
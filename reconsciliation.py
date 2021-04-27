import datetime

import utils

def main():
    # get a name and open the output log file
    file_name = utils.file_name_generator(12, False)
    log_file = utils.generate_log_file(file_name)

    failed_entries_file_name = utils.file_name_generator(12, True)
    failed_entries_file = utils.generate_log_file(failed_entries_file_name)

    #process_paygaer_order_files("taxi_lines_42.xlsx", log_file, failed_entries_file)

    # close the file
    log_file.close()
    failed_entries_file.close()

main()
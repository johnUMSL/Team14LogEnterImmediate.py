from constatnts import SUMMARY, ACTIVITY_CODES, GOODBYE
from helpers import readyToContinue, clear_console
from csv_functions import find_csv_files, validate_csv_file,append_csv_file
from activity_log_functions import log_activity,log_number_of_people,log_notes
from time_log_functions import log_time, create_log_entries

# datetime import is for testing create_log_entries()
# from datetime import datetime

def main():
  clear_console()
  print(SUMMARY)
  readyToContinue()

  csv_file = find_csv_files()
  validate_csv_file(csv_file)

  activity_code = log_activity(ACTIVITY_CODES)
  number_of_people = log_number_of_people()
  note = log_notes(activity_code)
  start, end = log_time()

  # The following are test variables for create_log_entries()
  # activity_code = "3"
  # number_of_people = 3
  # note = "abcde"
  # start = datetime(2024,9,27,10,25)
  # end = datetime(2024,9,28,0,25)

  log_entries = create_log_entries(start, end, number_of_people, activity_code, note)
  append_csv_file(csv_file, log_entries)
  for entry in log_entries:
    print(','.join(map(str, entry)))
  
  print(GOODBYE)

if __name__=='__main__':
  main()
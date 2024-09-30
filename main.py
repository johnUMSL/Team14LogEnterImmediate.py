# Class: CS 4500, Phase 1B Program Name: Team14LogEnterImmediate.py, Date: 09/01/2024, Last Modified: 09/29/2024
# Programmed using Python 3.10.4, the development environment is Visual Studio Code.
# Primarily programmed by John Garrett. Received help with comment structure from Dat Nguyen. Received help with function 
# def create_log_entries() from Salim Husain

# Description of program:This program confirms the existence and proper formatiing of a CSV file. 
# It takes, and validates, inputs from an interactive user and from that file. 
# When the user runs this program, the program starts and stop a virtual clock, 
# and automatically enters the activity abd time information into the activity log. 
# The input is displayed on the screen and written to a CSV file.

# Build instructions: 
# To compile and build an executable file for this program, make sure you have pyinstaller in your virtual environment.
# Once your virtual environment has been activated, you can install pyinstaller by typing in the terminal "pip install pyinstaller" (Do not include "")
# Once installed, then type in the terminal "pyinstaller --onefile main.py" (Do not include "")
# The file will build and an executable file named "main.exe" and save it in the dist folder within your project.
# main.exe can be moved and run from any location, but the CSV file you are reading MUST be in the same folder.
# The external CSV file I am using is named GarrettJohnLog.csv
# In your terminal, navigate to the location of main.exe, confirm the existense of your properly named CSV file, 
# and run the executable using the command "./main.exe".

# Resources used in program:
# 1. https://dev.to/nati_thinks_tech/map-and-join-and-strings-2p8 - Helped me figure out how to get all objects in a list and transform them into strings with map() and join()
# 2. https://stackoverflow.com/questions/59497109/is-there-a-python-3-command-to-clear-the-output-console - Used to clear console. Either Windows or Linux/Mac.
# 3. https://stackoverflow.com/questions/68210148/os-path-abspath-from-where-is-executed - Helped me to figure out how to find the current directory.
# 4. https://regex101.com/ - Great regex tester tool, which can help you find the appropriate regex patterns
# 5. https://stackoverflow.com/questions/2363731/how-to-append-a-new-row-to-an-old-csv-file-in-python - Helped me figure out how to append rows to a CSV file
# 6. https://docs.python.org/3/library/re.html#match-objects - helped me write functions to match regex patterns and filenames
# 7. https://strftime.org/ - Great cheat sheet to help with strftime() from datetime module

# imports for constants, helper functions, and modules
from constatnts import SUMMARY, ACTIVITY_CODES, GOODBYE
from helpers import readyToContinue, clear_console
from csv_functions import find_csv_files, validate_csv_file,append_csv_file
from activity_log_functions import log_activity,log_number_of_people,log_notes
from time_log_functions import log_time, create_log_entries

# The main function controls the workflow for logging 
# an activity, printing it to the screen, 
# and appending it to a CSV file.
def main():
  clear_console() # clear the console
  print(SUMMARY) # print the SUMMARY from constants.py
  readyToContinue() # wait for user to procedd by entering input

  csv_file = find_csv_files() # find one properly named CSV file
  validate_csv_file(csv_file) # validate the found CSV file's contents

  activity_code = log_activity(ACTIVITY_CODES) # propmt user to select an activity code from ACTIVITY_CODES in constants.py. 
  number_of_people = log_number_of_people() # propmt user to select number of people in activity
  note = log_notes(activity_code) # prompt user to create a note for the activity log
  start, end = log_time() # log the start and end time of activity

  log_entries = create_log_entries(start, end, number_of_people, activity_code, note) # Create log entries
  append_csv_file(csv_file, log_entries) # append the log entries to the CSV file

  # loop throug each entry (may be 1 or 2 entries).
  # the elements in the array are converted to strings, 
  # seperated by commas, and printed to the screen
  for entry in log_entries:
    print(','.join(map(str, entry))) # Resource #1
  
  print(GOODBYE)

# entry point
if __name__=='__main__':
  main()
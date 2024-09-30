# Module and constants import
from datetime import datetime
from constatnts import YES, NO

# Function to log the start and end times of an activity.
def log_time():
  start = datetime.now() # Capture the start datetime
  print(f"\nStart datetime: {start}") 
  input("\nPress Enter when finished Activity and ready to log......\n")
  
  check = True
  while check == True: # Prompt user until they enter a value from YES array in constants.py
    double_check = input("Have you finished the activity?\n"+
                        f"Please enter {YES} if finished.\n"+
                        f"Please enter {NO} to continue.\n")
    if double_check in YES:
      end = datetime.now() # Capture end datetime
      print(f"\nEnd datetime: {end}\n")
      check = False # Flip flag to end while loop
      return start, end
    elif double_check in NO: # Prompt user to press enter if they selected a value from NO array in constants.py
      input("\nPress Enter when finished Activity and ready to log......\n")
    else: # Print error message for invalid input
      print("\nInvalid entry.")

# Function to create log entries based on the start and end times of the activity.
def create_log_entries(start: datetime, end: datetime, number, code, note):
  log_entries = []
  
  # If the start and end times are on the same date, create a single log entry
  if start.date() == end.date():
    date = start.strftime('%x') # Resource #7
    start = start.strftime('%H:%M') # Resource #7
    end = end.strftime('%H:%M') # Resource #7
    log_entries.append([date, start, end, number, code, note])
  else: # If the times span across midnight, create two separate log entries
    # First entry: From start time to 23:59 on the first day
    date_one = start.strftime('%x') # Resource #7
    start_one = start.strftime('%H:%M') # Resource #7
    end_one = "23:59"
    log_entries.append([date_one, start_one, end_one, number, code, note]) # Append list

    # Second log entry starting @ 00:00 to the end time on the second day
    date_two = end.strftime('%x') # Resource #7
    start_two = "00:00"
    end_two = end.strftime('%H:%M') # Resource #7
    log_entries.append([date_two, start_two, end_two, number, code, note]) # Append list
    
  return log_entries # Return the list of log entries (either one or two entries)
from datetime import datetime
from constatnts import YES, NO

def log_time():
  start = datetime.now()
  print(f"\nStart datetime: {start}")
  input("\nPress Enter when finished Activity and ready to log......\n")
  check = True
  
  while check == True:
    double_check = input("Have you finished the activity?\n"+
                        f"Please enter {YES} if finished.\n"+
                        f"Please enter {NO} to continue.\n")
    if double_check in YES:
      end = datetime.now()
      print(f"\nEnd datetime: {end}\n")
      check = False
      return start, end
    elif double_check in NO:
      input("\nPress Enter when finished Activity and ready to log......\n")
    else:
      print("\nInvalid entry.")

def create_log_entries(start: datetime, end: datetime, number, code, note):
  log_entries = []
  
  if start.date() == end.date():
    date = start.strftime('%x')
    start = start.strftime('%H:%M')
    end = end.strftime('%H:%M')
    log_entries.append([date, start, end, number, code, note])
  else:  
    date_one = start.strftime('%x')
    start_one = start.strftime('%H:%M')
    end_one = "23:59"
    log_entries.append([date_one, start_one, end_one, number, code, note])

    date_two = end.strftime('%x')
    start_two = "00:00"
    end_two = end.strftime('%H:%M')
    log_entries.append([date_two, start_two, end_two, number, code, note])
    
  return log_entries





  
  
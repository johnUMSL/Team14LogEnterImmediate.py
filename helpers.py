import os

def clear_console():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def readyToContinue():
  check = True
  while check == True:
    user_input = input("Please enter 'y' or 'Y' when ready to continue.\n")
    if user_input.lower() != 'y':
      print("Invalid entry.")
    else:
      print("Beginning file search.....")
      check = False
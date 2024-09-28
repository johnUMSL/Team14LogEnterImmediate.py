
def log_activity(codes):
  for code, description in codes.items():
    print(f"Activity Code: {code} - {description}")
  while True:
    activity_code = input("Please select the Activity Code (0-9 or A-D) from " + 
                       "the menu above to begin logging an activity\n")
    if activity_code in codes:
      return activity_code
    else:
      print("Invalid entry.")


def log_number_of_people():
  while True:
    number_of_people = input("Please enter the number of people (1-50) involved in the activity.\n")
    try:
      number_of_people = int(number_of_people)
      if number_of_people > 0 and number_of_people < 51:
        return number_of_people
      else:
        print("Invalid entry.")
    except:
      print("Invalid entry.")


def log_notes(code):
  started_typing = False
  while True:
    if code == "D":
      notes = input("A note is reguired for 'Other'. Please enter a note 80 or fewer characters. " +
                  "Do not include commas in notes.\n").strip()
      if notes != "" and len(notes) < 81 and "," not in notes:
        return notes
      else:
        print("Invalid entry.")
    else:
      notes = input("Enter a note 80 or fewer characters, or press enter to Skip. " +
                  "Do not include commas in notes.\n").strip()
      if notes != "":
          started_typing = True
      if notes == "" and started_typing == False:
        return None
      elif notes == "" and started_typing == True:
        print("A note was started. It is no longer optional. A non-empty note must be entered.")
      elif len(notes) > 80 or "," in notes:
        print("Invalid entry")
      else:
        return notes


def log_activity(codes):
  # Loop through each activity code and its description in ACTIVITY_CODES.
  # Print the activity code along with its corresponding description.
  for code, description in codes.items():
    print(f"Activity Code: {code} - {description}")
  while True: # Prompt user to input an activity code until a code is valid.
    activity_code = input("Please select the Activity Code (0-9 or A-D) from " + 
                       "the menu above to begin logging an activity\n")
    if activity_code in codes: # Return user input if it matches one of the valid codes in ACTIVITY_CODES
      return activity_code
    else: # Print an error message and prompt until user input is invalid
      print("Invalid entry.")


def log_number_of_people():
  while True: # Prompt user to input the number of people until valid input is entered
    number_of_people = input("Please enter the number of people (1-50) involved in the activity.\n")
    try:
      number_of_people = int(number_of_people) # Try converting the input to an integer
      if number_of_people > 0 and number_of_people < 51: # Return user input if integer is within the valid range
        return number_of_people
      else:
        print("Invalid entry.")
    except: # If input cannot be converted to an integer, print error message
      print("Invalid entry.")


def log_notes(code):
  started_typing = False # Flag to track if the user has attempted to submit a note
  while True: # Prompt user for a note until a valid input is entered
    if code == "D":  # If activity code is "D", a note is required
      notes = input("A note is reguired for 'Other'. Please enter a note 80 or fewer characters. " +
                  "Do not include commas in notes.\n").strip()
      # Check that the note is non-empty, less than 81 characters, and does not contain commas
      if notes != "" and len(notes) < 81 and "," not in notes:
        return notes
      else:
        print("Invalid entry.")
    else: # If activity code is not "D", a note is optional
      notes = input("Enter a note 80 or fewer characters, or press enter to Skip. " +
                  "Do not include commas in notes.\n").strip()
      if notes != "": # Check if user attempted to submit a note
          started_typing = True # Flip flag; note submission has been attempted
      if notes == "" and started_typing == False: # No note submission was previously, or currently attempted.
        return None # Skip Note
      elif notes == "" and started_typing == True:
        print("A note was started. It is no longer optional. A non-empty note must be entered.")
      # Validate that the note is within the 80-character limit and has no commas
      elif len(notes) > 80 or "," in notes:
        print("Invalid entry")
      else: # return note if valid
        return notes

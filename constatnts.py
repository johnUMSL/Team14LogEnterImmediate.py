SUMMARY = """\nThis program is an activity log that takes inputs from an interactive user, and from an external file. 
The program outputs to the screen and to an external file. It allows the user to start and stop a 
virtual clock, and automatically enter the log information into the activity log in real time.
"""

ACTIVITY_CODES = {
  "0": "Reading Canvas Site or Textbook",
  "1": "Studying Using a Practice Quiz",
  "2": "Taking a Scoring Quiz",
  "3": "Participating in a Canvas Discussion, DX",
  "4": "Meeting with your Team",
  "5": "Working on Documentation",
  "6": "Working on Designs",
  "7": "Programming",
  "8": "Working on a Test Plan or Doing Testing",
  "9": "Studying for the Final Exam",
  "A": "Conferring with the Instructor Outside of a Team Meeting",
  "B": "Working on a Mini-Lecture Video or Reading",
  "C": "Viewing a Video or Website that is not a Mini-Lecture, but Relevant to the Course",
  "D": "Other" 
}

YES = ['Y', 'y', 'Yes', 'yes']
NO = ['N', 'n', 'No', 'no']

GOODBYE = """\nAbove is the line (or lines) which have been appended to your Activity Log file.
Thank you for logging your activity.
Goodbye.\n"""

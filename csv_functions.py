import os # operating system import
import re # regular expression import
from pathlib import Path # filesystem path import
import csv # csv import

# Function to find a correctly formatted CSV file in the current directory
def find_csv_files():
  base_path = os.path.abspath(".")  # capture absolute path of the current directory, Resource #3
  csv_files = list(Path(base_path).glob("*.csv")) # List all CSV files in the directory using pathlib's glob method
  regex_pattern = "[A-Z][a-z]*[A-Z][a-z]*Log\.csv"  # Capture regex to match CSV file names in the format: "LastnameFirstname.csv", Resource #4
  files_matching_pattern = [] # Empty list to store files that match the regex pattern
  
  # Loop over CSV files and check if they match the the format: "LastnameFirstname.csv"
  for file in csv_files:
    if re.match(regex_pattern, file.name):
      files_matching_pattern.append(file) # Append the file if it matches the format "LastnameFirstname.csv"
  
  # Raise an exception if no "LastnameFirstname.csv" files are found
  if not files_matching_pattern:
    raise Exception("There is no CSV file with the correctly formatted name.")
  
  # Raise an exception if more than one "LastnameFirstname.csv" files are found
  if len(files_matching_pattern) > 1:
    raise Exception("There is more than one CSV file with the correctly formatted name.")
  return files_matching_pattern[0] # Return the first (and only) "LastnameFirstname.csv" file

# Function to validate the contents of the CSV file
def validate_csv_file(csv_file):
  name_regex_pattern = "[A-Z][a-z]*,[A-Z][a-z]*" # Capture regex to match format "Lastname,Firstname". Resource #4
  course_regex_pattern = "[A-Z]{2}\s\d{4}" # Capture regex to match format Course Codes. For example, "CS 4500". Resource #4
  name_in_line = [] # Empty list to store name information
  course_in_line = [] # Empty list to store course code information

  try:
    with open(csv_file, 'r') as file:
      lines = file.readlines() # Read all lines from the CSV file
  except:
    raise Exception("CSV File is not formatted correctly.")
  
  # Ensure the CSV file has at least two lines (name and class ID)
  if len(lines) < 2:
    raise Exception("There should be at least two lines of data in the CSV file.")
  
  # Validate the first line with name_regex_pattern. Resource #6
  if re.match(name_regex_pattern, lines[0]):
    # Split the first line by commas, add non-empty, stripped values to name_in_line list
    for data in lines[0].split(','):
      data = data.strip()
      if data:
        name_in_line.append(data)
    print(f"\nLast Name, First Name: {name_in_line[0]}, {name_in_line[1]}") # Output last and first name from name_in_line list
  else:
    raise Exception("The name data in the CSV file is not formatted correctly.") # Raise an exception if the name format is incorrect
  
  # Validate the second line with course_regex_pattern. Resource #6
  if re.match(course_regex_pattern, lines[1]):
    for data in lines[1].split(','):
      data = data.strip()
      if data:
        course_in_line.append(data)
    print(f"Class ID: {course_in_line[0]}\n")
  else:
    raise Exception("The Class ID data in the CSV file is not formatted correctly.")   

# Function to append log entries to the CSV file
def append_csv_file(csv_file, log_entries):
  # Open the CSV file in append mode ('a') and write the log entries
  with open(csv_file, 'a', newline='') as file:
    append = csv.writer(file) # Create a CSV writer object
    append.writerows(log_entries) # Write the rows (log entries) to the file. Resource #5

    
      

  
  
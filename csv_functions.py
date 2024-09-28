import os
import re
from pathlib import Path
import csv

def find_csv_files():
  base_path = os.path.abspath(".")
  csv_files = list(Path(base_path).glob("*.csv"))
  regex_pattern = "[A-Z][a-z]*[A-Z][a-z]*Log\.csv"
  files_matching_pattern = []
  for file in csv_files:
    if re.match(regex_pattern, file.name):
      files_matching_pattern.append(file)
  if not files_matching_pattern:
    raise Exception("There is no CSV file with the correctly formatted name.")
  if len(files_matching_pattern) > 1:
    raise Exception("There is more than one CSV file with the correctly formatted name.")
  return files_matching_pattern[0]

def validate_csv_file(csv_file):
  name_regex_pattern = "[A-Z][a-z]*,[A-Z][a-z]*"
  course_regex_pattern = "[A-Z]{2}\s\d{4}"
  name_in_line = []
  course_in_line = []
  try:
    with open(csv_file, 'r') as file:
      lines = file.readlines()
  except:
    raise Exception("CSV File is not formatted correctly.")
  if len(lines) < 2:
    raise Exception("There should be at least two lines of data in the CSV file.")
  if re.match(name_regex_pattern, lines[0]):
    for data in lines[0].split(','):
      data = data.strip()
      if data:
        name_in_line.append(data)
    print(f"\nLast Name, First Name: {name_in_line[0]}, {name_in_line[1]}")
  else:
    raise Exception("The name data in the CSV file is not formatted correctly.")     
  if re.match(course_regex_pattern, lines[1]):
    for data in lines[1].split(','):
      data = data.strip()
      if data:
        course_in_line.append(data)
    print(f"Class ID: {course_in_line[0]}\n")
  else:
    raise Exception("The Class ID data in the CSV file is not formatted correctly.")   

def append_csv_file(csv_file, log_entries):
  with open(csv_file, 'a', newline='') as file:
    append = csv.writer(file)
    append.writerows(log_entries)

    
      

  
  
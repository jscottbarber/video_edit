import os
import calendar
import datetime

ROOT_FOLDER = 'D:\\Video\\Arlo'
int_year = int(datetime.datetime.now().year)
int_month = int(datetime.datetime.now().month)

if os.path.exists(ROOT_FOLDER):
  print(f"Found Folder: {ROOT_FOLDER}")

  c = calendar.TextCalendar(calendar.SUNDAY)

  #loop through all the days in the specified month, starting with 1
  for i in c.itermonthdays(int_year, int_month):
    if i > 0:  #itermonthdays returns a printable calendar so we must ignore 0's
      folder_name = f"{ROOT_FOLDER}\\{int_year}\\{int_year}-{int_month:02}-{i:02}"
      print("Creating Folder: " + folder_name)
      if not os.path.exists(folder_name):
        os.makedirs(folder_name)
      else:
        print("   Skipping, Folder Already Existed: " + folder_name)
else:
  print(f"Folder {ROOT_FOLDER} not found.  Program exiting.")


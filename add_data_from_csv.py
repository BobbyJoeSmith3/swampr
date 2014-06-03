#add_data_from_csv.py

from app import db, models
import csv

with open('userinfo2.csv', 'rb') as csvfile:
	event_file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in event_file_reader:
		newuser = models.User(firstname = row[0], lastname = row[1], username = row[2])
		db.session.add(newuser)
db.session.commit()
print "done!"

# Working with a csv file always has these parts:
#---------------------------------------------------
# A line (like line 7) to open the file that tells the computer which file 
# you want to open and some options to help it understand how that file is laid out.

# A line (like line 8) that tells Python how to save the info from the csv in its own
# language.

# A line (like line 9) that starts the for loop that will cycle through all the rows
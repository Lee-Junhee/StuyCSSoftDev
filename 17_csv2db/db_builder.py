#Junhee Lee, Ray Lee
#SoftDev pd1
#K17 -- No Trouble
#2019-10-08

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="abettertalos.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops




# with open('students.csv', newline='') as studentscsvfile:
#     studentscsvreader = csv.DictReader(studentscsvfile)
#     for row in studentscsvreader:
#         print(row['name'], row['age'], row['id'])

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >


command = "CREATE table courses(code TEXT, mark INTEGER, id INTEGER)"        # test SQL stmt in sqlite3 shell, save as string
c.execute(command) 
with open('courses.csv', newline='') as coursescsvfile:
    coursescsvreader = csv.DictReader(coursescsvfile)
    for row in coursescsvreader:
        print(row['code'], row['mark'], row['id'])
        c.execute("INSERT INTO courses VALUES (\"{}\", \"{}\", \"{}\");".format(row['code'], row['mark'], row['id']))

command = "CREATE table students(name TEXT, age INTEGER, id INTEGER)"        # test SQL stmt in sqlite3 shell, save as string
c.execute(command) 
with open('students.csv', newline='') as studentscsvfile:
    studentscsvreader = csv.DictReader(studentscsvfile)
    for row in studentscsvreader:
        print(row['name'], row['age'], row['id'])
        c.execute("INSERT INTO students VALUES (\"{}\", \"{}\", \"{}\");".format(row['name'], row['age'], row['id']))

#==========================================================

db.commit() #save changes
db.close()  #close database

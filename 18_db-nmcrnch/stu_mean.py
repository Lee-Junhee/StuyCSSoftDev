#Pratham Rawat
#SoftDev pd1
#K17 :: No
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="schooldata.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

studentData = c.execute("SELECT students.name, courses.mark FROM students,courses WHERE students.id = courses.id;")
sums = {}
for record in c.fetchall():
    
    
def insertData(courseID, student, mark):
    c.execute("SELECT id FROM students WHERE name = {}".format(student))
    id = c.fetchone()[1]
    c.execute("INSERT INTO courses(code, mark, id) VALUES {} {} {};".format(courseID, mark, id)

#==========================================================
db.commit() #save changes
db.close()  #close database

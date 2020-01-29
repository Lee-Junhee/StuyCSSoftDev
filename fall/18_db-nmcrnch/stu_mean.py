#Junhee Lee, Pratham Rawat
#SoftDev pd1
#K18 :: No
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="schooldata.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

get = "SELECT students.name, courses.mark, students.id FROM students,courses WHERE students.id = courses.id;"
stuData = {}
stuId = {}
for row in c.execute(get):
    stuData[row[0]] = []
for row in c.execute(get):
    stuData[row[0]].append(row[1])
    stuId[row[0]] = row[2]
#print(stuData)

stuAvg = {}
for key in stuId.keys():
    stuAvg[key] = sum(stuData[key]) / len(stuData[key])
#print(stuAvg)

for name in stuId.keys():
    row = "{}({}): {}".format(name, stuId[name], stuAvg[name])
    print(row)

cmd = "DROP TABLE stu_avg;"
c.execute(cmd)
cmd = "CREATE TABLE stu_avg(id INTEGER PRIMARY KEY, avg INTEGER);"
c.execute(cmd)

for name in stuData.keys():
    cmd = "INSERT INTO stu_avg VALUES ({}, {});".format(stuId[name], stuAvg[name])
    c.execute(cmd)
#def insertData(courseID, student, mark):
#    c.execute("SELECT id FROM students WHERE name = {}".format(student))
#    id = c.fetchone()[1]
#    c.execute("INSERT INTO courses(code, mark, id) VALUES {} {} {};".format(courseID, mark, id)

#==========================================================
db.commit() #save changes
db.close()  #close database

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
try: #Code to load courses
    csv = open("courses.csv", "r")
    c.execute("CREATE TABLE IF NOT EXISTS courses(code STRING, mark INTEGER, id INTEGER)") #Creates table courses
    c.execute("DELETE FROM courses WHERE True")    # deletes all data in order to load all data in (no duplicates)
    header = True
    for line in csv:
        if not header:
            fields = line.strip().split(',')
#            print("INSERT INTO courses(code, mark, id) VALUES (' " + fields[0] +"', " + fields[1] +", " + fields[2] +")")
            c.execute("INSERT INTO courses(code, mark, id) VALUES (' " + fields[0] +"', " + fields[1] +", " + fields[2] +")") #inserts data into database
        else:
            header = not header
except Exception as e:
    print(e)
    
try: #code to load students
    csv = open("students.csv", "r")

    c.execute("CREATE TABLE IF NOT EXISTS students(name STRING, age INTEGER, id INTEGER)")
        
    c.execute("DELETE FROM students WHERE True")
        
    header = True
    for line in csv:
        if not header:
            fields = line.strip().split(',')
#            print("INSERT INTO students(name, age, id) VALUES (' " + fields[0] +"', " + fields[1] +", " + fields[2] +")")
            c.execute("INSERT INTO students(name, age, id) VALUES (' " + fields[0] +"', " + fields[1] +", " + fields[2] +")")
        else:
            header = not header
except Exception as e:
    print(e)
#==========================================================
finally:
    db.commit() #save changes
    db.close()  #close database




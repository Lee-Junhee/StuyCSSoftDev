#Junhee Lee
#SoftDev1 pd1
#K08 -- Lemme Flask You Sump'n
#2019-09-18

from flask import Flask, render_template
import csv,random

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return '''
        <head>
        <title>Main</title>
        </head>
        <body>
        <p>This was made using Flask</p>
        <p><a href="./state">Subpage0</a></p>
        <p><a href="./church">Subpage1</a></p>
        <p><a href="./static/staticTest.html">static page test</a></p>
        </body>
    '''

@app.route("/state")
def preamb():
    print(__name__) #prints "__main__"
    return "We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America."

@app.route("/church")
def gen1():
    print(__name__) #prints "__main__"
    return "In the beginning God created the heavens and the earth."

coll = [0,1,1,2,3,5,8]
@app.route("/my_foist_template")
def disp():
    print(__name__)
    return render_template("seed.html",
            foo="fooooo",
            collection=coll)

@app.route("/occupyflaskst")
def occupations():
    rows = []
    with open('data/occupations.csv', 'r') as csvFile:
        csvreader = csv.reader(csvFile)
        for row in csvreader:
            rows.append(row)

    dictionary = {}
    for item in rows[1: len( rows) - 1]:
        key = item[0]
        value = float( item[1])
        dictionary[ key] = value
    chosen = random.random() * float(rows[len(rows) - 1][1])
    #print(chosen) #verification step
    for occupation in dictionary.keys():
        chosen -= dictionary[occupation]
        if chosen <= 0:
            random_occupation =  occupation   
            break
    
    occList=[]
    for occ in dictionary.keys():
        occList.append((occ, dictionary[occ]))

    return render_template("table.html",
            title="Occupation Data",
            heading="Occupations in the United States and Percentage of Workforce",
            occupation=random_occupation,
            tHead=['Occupation Title','Percentage of Workforce'],
            entries=occList)

if __name__ == "__main__":
    app.debug = True 
    app.run()

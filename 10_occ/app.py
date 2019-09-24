#Junhee Lee, Michael Lin
#SoftDev1 pd1
#K10 -- Jinja Tuning
#2019-09-20

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
        </body>
    '''

@app.route("/occupyflaskst")
def occupations():
    rows = []
    with open('data/occupations.csv', 'r') as csvFile:
        csvreader = csv.reader(csvFile)
        for row in csvreader:
            rows.append(row)

    occDict = {}
    for item in rows[1: len( rows) - 1]:
        key = item[0] #key is the occupation name
        occDict[key] = (float(item[1]),item[2]) #key is a tuple (percentage, link)
    chosen = random.random() * float(rows[len(rows) - 1][1]) #random number [0.0, 1.0] multiplied by total

    for occupation in occDict.keys():
        chosen -= occDict[occupation][0] #keep subtracting the percentage of occupation
        if chosen <= 0: #if the chosen number is less than or equal to zero, then we found the occupation
            random_occupation =  occupation   
            break
        

    return render_template("table.html",
            title="Occupation Data",
            header=("Junhee Lee, Michael Lin", "SoftDev1 pd1", "K10 -- Jinja Tuning", "2019-09-20"),
            heading="Occupations in the United States and Percentage of Workforce",
            occupation=random_occupation,
            tHead=['Occupation Title','Percentage of Workforce'],
            entries=occDict)

if __name__ == "__main__":
    app.debug = True 
    app.run()
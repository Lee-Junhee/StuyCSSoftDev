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
        <p><a href="./occupyflaskst">Occupations</a></p>
        </body>
    '''

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
        value = (float( item[1]),item[2])
        dictionary[ key] = value
    chosen = random.random() * float(rows[len(rows) - 1][1])
    #print(chosen) #verification step
    for occupation in dictionary.keys():
        chosen -= dictionary[occupation][0]
        if chosen <= 0:
            random_occupation =  occupation   
            break
    
    occList=[]
    for occ in dictionary.keys():
        occList.append((occ,
            dictionary[occ][0],
            dictionary[occ][1]))

    return render_template("table.html",
            title="Occupation Data",
            heading="Junhee Lee, Michael Lin<br>SoftDev pd1<br>K10 -- Jinja Tuning<br>2019-09-23",
            occupation=random_occupation,
            tHead=['Occupation Title','Percentage of Workforce','Link'],
            entries=occList)

if __name__ == "__main__":
    app.debug = True 
    app.run()

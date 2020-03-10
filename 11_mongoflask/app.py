from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import json

app = Flask(__name__)
client = MongoClient()
db = client.HoR

def loadFromFile():
    file = open("role.json", "r")
    lines = file.read()
    dictionary = json.loads(lines)
    for object in dictionary['objects']:
        db.government.insert_one(object)

#loadFromFile()

print('loaded!')

@app.route('/')
def main():
    return render_template('search.html')

@app.route('/results', methods=['POST'])
def results():
    if request.form['party'] and request.form['district']:
        r = db.find({'$and': [{'party': request.form['party']}, {'district': request.form['district']}]})
    elif request.form['party']:
        r = db.find({'party': request.form['party']})
    elif request.form['district']:
        r = db.find({'district': request.form['district']})
    else:
        return redirect('/')
    return render_template('results.html',
            results = r)

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0')

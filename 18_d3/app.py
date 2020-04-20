#Benjamin Avrahami, Junhee Lee
#SoftDev2 pd9, 1
#K18 :: Come Up For Air
#2020-04-06    

from flask import Flask, render_template, request, redirect
import csv
import json

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/data', methods=['POST'])
def load():
    year = request.form['year']
    with open('static/data/school_scores.csv') as file:
        scorereader = csv.reader(file, delimiter=',')
        raw = [row for row in scorereader if row[0] == year]
    dataset = dict()
    for data in raw:
        dataset[data[2]] = int(data[3]) + int(data[5])
    return json.dumps(dataset)


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0')

import json
import urllib.request

from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/rickandmorty')
def rickandmorty():
    try:
        data = json.loads(urllib.request.urlopen('https://rickandmortyapi.com/api/character/').read())

        return render_template('rickandmorty.html', data=data)

    except BaseException:
        return render_template('error.html')

@app.route("/currency")
def currency():
    try:
        data = json.loads(urllib.request.urlopen('https://api.exchangerate-api.com/v4/latest/USD').read())
        return render_template('exchange.html', data=data)
    except BaseException:
        return render_template('error.html')

@app.route('/countries')
def countries():
    try:
        data = json.loads(urllib.request.urlopen('https://restcountries.eu/rest/v2/').read())

        return render_template('countries.html', data=data)

    except BaseException:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)

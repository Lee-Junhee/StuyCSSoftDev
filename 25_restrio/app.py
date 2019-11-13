import json
import urllib.request

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/randm')
def rickandmorty():
    try:
        data = json.loads(urllib.request.urlopen('https://rickandmortyapi.com/api/character/').read())

        return render_template('rickandmorty.html', data=data)

    except BaseException:
        return render_template('error.html')

@app.route("/pkmn")
def pokemon():
    try:
        raw = urllib.request.urlopen('https://pokeapi.co/api/v2/pokemon').read()
        print("get raw data")
        data = json.loads(raw)
        return render_template('rickandmorty.html', data=data)
    except BaseException:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from json import loads
from urllib.request import urlopen
app = Flask(__name__)

@app.route("/")
def renderAPI():
    u = urlopen("https://api.nasa.gov/planetary/apod?api_key=6lP4sG1PtWFAweeObI0YVxwKHewiKiJFUGeSQptR&date=2018-01-01")
    response = u.read()
    data = loads(response)
    return render_template("root.html",
            pic = data['hdurl'],
            content = data['explanation'])

if __name__ == "__main__":
    app.debug = True 
    app.run()

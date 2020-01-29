#Junhee Lee
#SoftDev1 pd1
#K08 -- Lemme Flask You Sump'n
#2019-09-18

from flask import Flask
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

if __name__ == "__main__":
    app.debug = True 
    app.run()

# Eric "Morty" Lau, Junhee Lee
# SoftDev1 pd1
# K15 -- Do I Know You?
# 2019-10-02

from flask import Flask, render_template, request, redirect, session, url_for
# import csv, random
app = Flask(__name__)
app.secret_key = "Test_Key"

team_name = "Plumbus"
roster = "Eric \"Morty\" Lau and Junhee Lee"

username = "user"
password = "passwd"

# with open('occupations.csv') as csv_file:
#     #code by Vishwaa, edited by kiran
#     read = csv.reader(csv_file, delimiter = ",")
#     dict = {}
#     displayData = {}
#     print(read)
#     for row in read:
#         if not (row[0] == "Job Class" or row[0] == "Total"):
#             dict[row[0]] = float(row[1])
#         displayData[row[0]] = row[1]

# #WEIGHTED RANDOM CHOICE (mortiestRick)

# # returns a weighted random element from a dictionary
# def weightedRandFromDict(dictionary):
#     keys = list(dictionary.keys())
#     weights = list(dictionary.values())

#     # return one(k=1) random job accounting for attached weights
#     # the [0] is needed because random.choices returns a list
#     return random.choices(keys,weights=weights,k=1)[0]

@app.route("/", methods=['GET'])
def root():
    if not 'login' in session:
        session['login'] = False
    if(session['login']):
        return redirect(url_for("welcome"))
    else:
        return render_template(
                "landing.html",
                team = team_name,
                names = roster
                )

@app.route("/welcome")
def welcome():
    return render_template(
            "response.html",
            team = team_name,
            names = roster,
            # username = request.args['username'],
            username = session['user'],
            method = request.method,
            url = url_for("logout")
    )
# @app.route("/occupy")
# def jobs():
#     job=weightedRandFromDict(dict)
#     return render_template(
#             "flaskStTemplate.html",
#             dict=displayData,
#             randomJob=job
#             )

@app.route("/auth", methods=["POST"])
def auth():
    # print("this is the app name", app, end="\n")
        # print("this is the request", request, end="\n")
        # print("this is the request headers", request.headers)
        # print("this is the request method", request.method, end="\n")
        # print("this is the request args", request.args, end="\n")
        # print("this is the request form", request.form, end="\n")
    if(request.form['username'] != username):
        session['reason'] = "username"
        return redirect(url_for("failure"))
    elif(request.form['password'] != password):
        session['reason'] = "password"
        return redirect(url_for("failure"))
    else:
        session['login'] = True
        session['user'] = request.form['username']
        return redirect(url_for("welcome"))

@app.route("/failure")
def failure():
    print("bad login")
    return render_template(
        "fail.html",
        reason = session['reason']
        )
@app.route("/logout")
def logout():
    session['login'] = False
    return redirect("/")

# @app.route("/ocupy")
# def misspell():
#     return redirect(url_for("jobs"))

# @app.route("/idunno")
# def redir():
#     return redirect("https://www.dailydot.com/wp-content/uploads/d42/e2/Screen20Shot202017-01-0320at204.52.2020PM.png")

if __name__ == "__main__":
    app.debug = True
    app.run()

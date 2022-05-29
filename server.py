from unicodedata import name
from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key ="Don't tell the secret key"

# @app.route('/')
# def working():
#     return("Server is running... better go catch it")
# confirming a connection and working

@app.route('/')
def index_form():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def info_intake():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    return redirect("/result")

@app.route('/result')
def display_info():
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True, port=5001)


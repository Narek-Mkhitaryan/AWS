#!/usr/bin/python3
from flask import Flask, render_template, url_for
app =Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Active')
def active():
    return render_template("active.html")

@app.route('/Link')
def Link():
    return render_template("Link.html")

@app.route('/Link_2')
def Link_2():
    return render_template("Link_2.html")
    
if __name__ == "__main__":
    app.run(debug=True)

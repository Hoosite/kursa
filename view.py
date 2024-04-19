from flask import render_template, url_for
from project import app

@app.route("/")
@app.route("/students")
def index():
    print(url_for('index'))
    return render_template('index.html')

@app.route("/teacher")
def teacher():
    print(url_for('teacher'))
    return render_template('teacher.html')
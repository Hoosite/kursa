from flask import Blueprint
from flask import render_template


about=Blueprint('about', __name__, template_folder='templates')

@about.route('/')
def abouts():
    return render_template('page/about.html')
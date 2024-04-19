from flask import Blueprint
from flask import render_template


mark=Blueprint('mark', __name__, template_folder='templates')

@mark.route('/')
def marks():
    return render_template('page/mark.html')
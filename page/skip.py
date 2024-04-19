from flask import Blueprint
from flask import render_template


skip=Blueprint('skip', __name__, template_folder='templates')

@skip.route('/')
def skips():
    return render_template('page/skip.html')
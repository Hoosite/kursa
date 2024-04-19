from flask import Blueprint
from flask import render_template

from models.student import students

me=Blueprint('me', __name__, template_folder='templates')


@me.route('/')
def mes():
    student=students[0]

    return render_template('page/me.html', stud=student)
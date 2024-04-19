from flask import Blueprint
from flask import render_template

from models.esubjects import esubject

syllabus=Blueprint('syllabus', __name__, template_folder='templates')

@syllabus.route('/')
def syllabuss():
    esub=esubject

    return render_template('page/syllabus.html', esub=esub)
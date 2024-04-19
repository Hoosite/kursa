from flask import Blueprint, render_template
from script.schedule_reader import read_schedule

schedule = Blueprint('schedule', __name__, template_folder='templates')

@schedule.route('/')
def display_schedule():
    # Путь к файлу Excel с расписанием
    file_path = 'script/rasp.xlsx'

    # Номер страницы с расписанием для нужной группы
    group_page = '1223_1227'

    # Чтение расписания из файла Excel
    schedule_group1, schedule_group2 = read_schedule(file_path, group_page)

    # Отображение расписания на веб-странице
    return render_template('schedule.html', schedule_group1=schedule_group1, schedule_group2=schedule_group2)

from flask import Blueprint, render_template, request
from script.schedule_reader import read_schedule

schedule = Blueprint('schedule', __name__, template_folder='templates')

@schedule.route('/')
def display_schedule():
    # Путь к файлу Excel с расписанием
    file_path = 'script/rasp.xlsx'
    
    # Получаем выбранную группу из параметров запроса
    group_page = request.args.get('group', '1223_1227')

    # Чтение расписания из файла Excel для выбранной группы
    schedule_group1, schedule_group2 = read_schedule(file_path, group_page)

    # Отображение расписания на веб-странице
    return render_template('schedule.html', selected_group=group_page, schedule_group1=schedule_group1, schedule_group2=schedule_group2)

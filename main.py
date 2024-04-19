from project import app

from page.me import me

from page.about import about

from page.mark import mark

from page.order import order

from page.schedule import schedule

from page.skip import skip

from page.syllabus import syllabus

import view

app.register_blueprint(me, url_prefix='/me')

app.register_blueprint(about, url_prefix='/about')

app.register_blueprint(mark, url_prefix='/mark')

app.register_blueprint(order, url_prefix='/order')

app.register_blueprint(schedule, url_prefix='/schedule')

app.register_blueprint(skip, url_prefix='/skip')

app.register_blueprint(syllabus, url_prefix='/syllabus')


if __name__ == '__main__':
    app.run()
class Esubject:
    def __init__(self, name, status, teacher):
        self.name=name
        self.status=status
        self.teacher=teacher
    
    def __repr__(self):
        return '<Esubject %' % self.name
    
esubject=[
    Esubject(name= 'Нереляционные бд', status='зачет', teacher='Пономарев'),
    Esubject(name= 'Технологии программирования', status='зачет', teacher='Пономарев'),
    Esubject(name= 'ЯП', status='зачет', teacher='Кузаев'),
    Esubject(name= 'ОС', status='зачет', teacher='Щипицын'),
    Esubject(name= 'Право', status='зачет', teacher='Довгяло'),
    Esubject(name= 'Методы исслед деятельности', status='зачет', teacher='Краузе'),
    Esubject(name= 'Системы наблюдения', status='зачет', teacher='Казаринова'),
    Esubject(name= 'Физра', status='зачет', teacher='Шилова'),
    Esubject(name= 'ВССТ', status='зачет с оценкой', teacher='Щипицын'),
    Esubject(name= 'Методы исслед деятельности', status='зачет с оценкой', teacher='Соловьева'),
    Esubject(name= 'Информатика', status='экзамен', teacher='Худорожков'),
    Esubject(name= 'ИСИТ', status='экзамен', teacher='Кузаев'),
]
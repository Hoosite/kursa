class Student:
    def __init__(self, id, name, surname, faculty, speciality, course, group, studak):
        self.id=id
        self.name=name
        self.surname=surname
        self.faculty=faculty
        self.speciality=speciality
        self.course=course
        self.group=group
        self.studak=studak
        
    def __repr__(self):
        return '<Student %' % self.name
    
students = [
    Student(id= '1', name='John', surname='Doe', faculty='Engineering', speciality='Computer Science', course=3, group=1, studak=12345),
    Student(id='2', name='Alice', surname='Smith', faculty='Medicine', speciality='Biology', course=2, group=2, studak=67890),
    # Добавить других студентов
]
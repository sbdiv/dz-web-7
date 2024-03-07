from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from main import Student, Subject, Grade, Teacher, Group

engine = create_engine('sqlite:///your_database.db')
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    result = session.query(Student, func.avg(Grade.value).label('avg_grade')) \
        .join(Grade).group_by(Student.id).order_by(func.avg(Grade.value).desc()).limit(5).all()
    return result

def select_2(subject_name):
    result = session.query(Student, func.avg(Grade.value).label('avg_grade')) \
        .join(Grade).join(Subject).filter(Subject.name == subject_name) \
        .group_by(Student.id).order_by(func.avg(Grade.value).desc()).first()
    return result

def select_3(subject_name):
    result = session.query(Group, func.avg(Grade.value).label('avg_grade')) \
        .join(Student).join(Grade).join(Lesson).join(Subject).filter(Subject.name == subject_name) \
        .group_by(Group.id).all()
    return result

def select_4():
    result = session.query(func.avg(Grade.value).label('avg_grade')).first()
    return result

def select_5(teacher_name):
    result = session.query(Subject).join(Teacher).filter(Teacher.name == teacher_name).all()
    return result

def select_6(group_name):
    result = session.query(Student).join(Group).filter(Group.name == group_name).all()
    return result

def select_7(group_name, subject_name):
    result = session.query(Student, Grade) \
        .join(Group).join(Grade).join(Lesson).join(Subject) \
        .filter(Group.name == group_name, Subject.name == subject_name).all()
    return result

def select_8(teacher_name):
    result = session.query(Teacher, func.avg(Grade.value).label('avg_grade')) \
        .join(Subject).join(Lesson).join(Grade).group_by(Teacher.id).filter(Teacher.name == teacher_name).all()
    return result

def select_9(student_name):
    result = session.query(Subject).join(Lesson).join(Grade).join(Student).filter(Student.name == student_name).all()
    return result

def select_10(student_name, teacher_name):
    result = session.query(Subject).join(Teacher).join(Lesson).join(Grade).join(Student) \
        .filter(Student.name == student_name, Teacher.name == teacher_name).all()
    return result

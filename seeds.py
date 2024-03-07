# seed.py
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Base, Group, Teacher, Subject, Student, Lesson, Grade

fake = Faker()

engine = create_engine('sqlite:///your_database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()

teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=fake.word(), teacher_id=fake.random_element(teachers).id) for _ in range(8)]
session.add_all(subjects)
session.commit()

students = [Student(name=fake.name(), group_id=fake.random_element(groups).id) for _ in range(50)]
session.add_all(students)
session.commit()

for student in students:
    for subject in subjects:
        lesson = Lesson(subject_id=subject.id)
        grade = Grade(value=fake.random_int(min=1, max=10), student=student, lesson=lesson)
        session.add_all([lesson, grade])

session.commit()

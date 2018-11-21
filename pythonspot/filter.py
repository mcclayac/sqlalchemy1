import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pythonspot.tabledef import *

engine = create_engine('sqlite:///student.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Select objects
for student in session.query(Student).filter(Student.firstname == 'Eric'):
    print("username: {} \t first name : {}\t last name: {} \t university: {}".format(
        student.username, student.firstname,student.lastname, student.university))

    # print
    # student.firstname, student.lastname

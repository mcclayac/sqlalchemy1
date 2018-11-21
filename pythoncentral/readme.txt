
Tutorial from pythoncentral
https://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/


##  ipython

from sqlalchemy_declarative import Person, Base, Address
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
session.query(Person).all()
person = session.query(Person).first()
person.name
 # Find all Address whose person field is pointing to the person object
session.query(Address).filter(Address.person == person).all()
session.query(Address).filter(Address.person == person).one()
address = session.query(Address).filter(Address.person == person).one()
address.post_code
history


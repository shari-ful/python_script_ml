from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_DB_HOST = os.environ.get('POSTGRES_DB_HOST')
POSTGRES_DB_USER = os.environ.get('POSTGRES_DB_USER')
POSTGRES_DB_PASS = os.environ.get('POSTGRES_DB_PASS')
POSTGRES_DB_PORT = os.environ.get('POSTGRES_DB_PORT')
POSTGRES_DB_NAME = os.environ.get('POSTGRES_DB_NAME')

postgres_uri = f"postgresql://{POSTGRES_DB_USER}:{POSTGRES_DB_PASS}@{POSTGRES_DB_HOST}:{POSTGRES_DB_PORT}/{POSTGRES_DB_NAME}"

engine = create_engine(postgres_uri)

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_data(name, age):
    person = Person(name=name, age=age)
    session.add(person)
    session.commit()

def retrieve_data():
    return session.query(Person).all()

def update_data(id, name, age):
    person = session.query(Person).filter_by(id=id).first()
    if person:
        person.name = name
        person.age = age
        session.commit()

def delete_data(id):
    person = session.query(Person).filter_by(id=id).first()
    if person:
        session.delete(person)
        session.commit()



session.close()

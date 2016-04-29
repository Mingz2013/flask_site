__author__ = 'zhaojm'
from sqlalchemy import Column, Integer, String

from app.database import Base



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    description = Column(String(120))

    def __init__(self, title=None, description=None):
        self.title = title
        self.description = description

    # def __repr__(self):
    #     return '<Activity %r' % (self.title)
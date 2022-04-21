from datetime import datetime
from db import Base
from sqlalchemy import Column, String, DateTime ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN

import hashlib

SQLITE3_NAME = "./db.sqlite3"

class User(Base):
    __tablename__ = 'user'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    username = Column('username', String(256))
    passworld = Column('password', String(256))
    mail = Column('mail', String(256))
    
    def __init__(self, username, password, mail):
        self.username = username
        self.passworld = hashlib.md5(password.encode()).hexdigest()
        self.mail = mail
    
    def __str__(self):
        return (self.id) + ':' + self.username

class Task(Base):
    __tablename__ = 'task'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key = True,
        autoincrement=True,
    )
    
    user_id = Column('user_id', ForeignKey('user.id'))
    
    
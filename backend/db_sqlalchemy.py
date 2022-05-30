from click import echo
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

print(sqlalchemy.__version__)
engine = create_engine('sqlite:///backend/db2.sqlite7', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)

    def __init__(self, user_id, first_name, last_name, age):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return "{self.first_name} {self.last_name}"
    
Base.metadata.create_all(engine)
SessionClass = sessionmaker(engine)
session = SessionClass()
use_a = User(user_id=4, first_name="first_a", last_name="last_a", age=20)
session.add(use_a)
session.commit()
users = session.query(User).all()

for user in users:
    print(f'{user.user_id} {user.first_name}  {user.last_name} {user.age}')

test = session.query(User).filter(User.user_id==4).first()
if test == None:
    print(test)
else:
    print(test.last_name)
session.close()
# users = session.query(User).all()
# for i in users:
#     print(i)
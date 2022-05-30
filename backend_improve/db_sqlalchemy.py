from click import echo
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
import main

print(sqlalchemy.__version__)
engine = create_engine('sqlite:////home/ericlab/tsuchida/study/web/fastapi_app/backend_improve/tsuchida_main.sqlite1', echo=True)

Base = declarative_base()



    
Base.metadata.create_all(engine)
SessionClass = sessionmaker(engine)
session = SessionClass()

user_a = main.Main_data(user_name="tsuchida", large_file=
session.add(user_a)
session.commit()

users = session.query(main.Tsuchida_data).all()
for user in users:
    print(f'{user.user_name} {user.password}')
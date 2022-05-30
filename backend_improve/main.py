from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy import Column, create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////home/ericlab/tsuchida/study/web/fastapi_app/backend_improve/tsuchida.sqlite1', echo=True)
Base = declarative_base()

class Web_data(BaseModel):
    username: str
    password: str

class Tsuchida_data(Base):
    __tablename__ = "login_data"
    user_name = Column(String(255), primary_key=True)
    password = Column(String(255))

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password



Base.metadata.create_all(engine)
SessionClass = sessionmaker(engine)
session = SessionClass()
# user_a = Tsuchida_data(user_name="tsuchida", password="j68VmsBW")
# session.add(user_a)
# session.commit()
app = FastAPI()
origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/data")
def post_data_func(post_data: Web_data):
    test = session.query(Tsuchida_data).filter(Tsuchida_data.user_name==post_data.username).first()
    password = ""
    print(post_data.username)
    print(post_data.password)
    if test == None:
        user = test
    else:
        user = test.user_name
        if test.password != post_data.password:
            password = None
        else:
            password = test.password
    return {
        "user": user,
        "password": password
    }
    # return {"mes": "trud"}
    

@app.post("/new_register")
def post_register_func(post_data: Web_data):
    test = session.query(Tsuchida_data).filter(Tsuchida_data.user_name==post_data.username).first()
    print("test")
    if test==None:
        add_data = Tsuchida_data(user_name=post_data.username, password=post_data.password)
        session.add(add_data)
        session.commit()
        return {"register_success": True}
    else:
        return {"register_success": False}





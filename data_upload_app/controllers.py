from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI(
    title='Fast API application',
    description="It`s great tutorial",
    version='0.9 beta'
)

templates = Jinja2Templates(directory='templates')
jinja_env = templates.env

def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

def style(request: Request):
    return templates.TemplateResponse('style.css', {'request': request})

def admin(request: Request):
    return templates.TemplateResponse('admin.html',
                                      {'request': request,
                                       'username': 'admin'})

def style_main(request: Request):
    return templates.TemplateResponse('style_main.css', {'request': request})
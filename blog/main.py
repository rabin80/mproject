from os import name
from fastapi import FastAPI,Depends,status,HTTPException,File,UploadFile,Request,Form
from pathlib import Path
import shutil,os
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app= FastAPI()
BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
app.mount("/static",StaticFiles(directory="static"),name="static")
app.mount("/images",StaticFiles(directory="images"),name="images")

@app.get("/blog",response_class=HTMLResponse)
def get_form(request:Request):
     return templates.TemplateResponse("test.html", {"request": request })


@app.post("/blog",response_class=HTMLResponse)
async def post_form(request:Request,file:UploadFile=File(...)):
  with open(f'{file.filename}',"wb") as buffer: 
    shutil.copyfileobj(file.file,buffer)
    
    return templates.TemplateResponse("test.html", {"request": request })

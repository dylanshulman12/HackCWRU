from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware
import json
from returnFile import *
from PIL import Image
from dotenv import load_dotenv
import uuid 

print("RUNNING \n")

# load the environment file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()



app.add_middleware(


    CORSMiddleware,


    allow_origins=["*"],  # React app origin


    allow_credentials=True,


    allow_methods=["*"],


    allow_headers=["*"],


)


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/api/upload")
async def saveFile(file: UploadFile = File(...)):
    print("UPLOADING FILE", file)

    extension = (".png", ".jpg", ".jpeg", ".heic")

    if not file.filename.lower().endswith(extension):
        return {"status": "Error: Only image files allowed"}

    fileName = file.filename

    filePath = os.path.join(UPLOAD_DIR, fileName)
    img = Image.open(file.file)
    img.save(filePath, format="PNG")

    print("FILE UPLOADED", file.filename)

    return {"status": "File Uploaded"}

@app.post("/api/info")
async def saveJSON(file: UploadFile = File(...)):
    fileName : str = file.filename

    filePath = os.path.join(UPLOAD_DIR, fileName)

    with open(filePath, "wb") as buffer:
        shutil.copfileobj(file.file, buffer)

@app.get("/api/returnInfo")
def serveJSON(file : str):
    # return "Hello"
    filePath = os.path.join(UPLOAD_DIR, file)

    if not os.path.exists(filePath):
        return {"status": filePath}
    
    return {"status": "error"}
    
    



@app.get("/api/files")
def servePNG(image: str):
    filePath = os.path.join(UPLOAD_DIR, image)

    if not os.path.exists(filePath):
        return {"status": filePath}
    
    return FileResponse(filePath, media_type = "image/png")

# @app.get("/api/location")
# def callReturnFile():
#     with open("./public/finalDataReturn.json", "r") as f:
#         data = json.load(f)
#     return data

@app.get("/api/plasticGet")
def callReturnFile(file : str, city, state, zipCode):  
    UPLOAD_DIR = "uploads/"
    return getReturnPlastic(os.path.join(UPLOAD_DIR, file), city, state, zipCode)




@app.get("/api/materialGet")
def callReturnFile(file, city, state, zipCode): 
    UPLOAD_DIR = "uploads/"
    return getReturnMaterial(os.path.join(UPLOAD_DIR, file), city, state, zipCode)

# @app.get("/api/location")
# def serveLocation(location : dict):
#     with open("location.json", "w") as f:
#         json.dump(location, f)
    
#     return {"status", "Success"}

 
@app.middleware("http")
async def add_user_id(request: Request, call_next):
    response = await call_next(request)

    if "user_id" not in request.cookies:
        user_id = str(uuid.uuid4())
        response.set_cookie(key = "user_id", value = user_id, htpponly = True)

    return response

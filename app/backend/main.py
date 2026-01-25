from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware
import json
from returnFile import *

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
    extension = (".png", ".jpg", ".jpeg", ".heic")

    # if not file.filename.lower().endswith(extension):
    #     raise HTTPException(status_code=400, detail="Only image files allowed")

    fileName : str = file.filename

    filePath = os.path.join(UPLOAD_DIR, fileName)

    with open(filePath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


@app.post("/api/info")
async def saveJSON(file: UploadFile = File(...)):
    fileName : str = file.filename

    filePath = os.path.join(UPLOAD_DIR, fileName)

    with open(filePath, "wb") as buffer:
        shutil.copfileobj(file.file, buffer)

@app.get("/api/returnInfo")
def serveJSON(file : str):
    return "Hello"
    filePath = os.path.join(UPLOAD_DIR, file)

    if not os.path.exists(filePath):
        return {"status": filePath}
    
    



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
    #return FileResponse("uploads/" + file, media_type = "image/png")
    
    
    result = getReturnPlastic("uploads/" + file, city, state, zipCode)
    resultPath = os.path.join(UPLOAD_DIR, result)


    print("hello world")
    return FileResponse(resultPath, media_type = "application/json")


@app.get("/api/materialGet")
def callReturnFile(file, city, state, zipCode): 
    print(file) 
    result = getReturnMaterial(file, city, state, zipCode)
    resultPath = os.path.join(UPLOAD_DIR, result)

    return FileResponse(resultPath, media_type = "application/json")

# @app.get("/api/location")
# def serveLocation(location : dict):
#     with open("location.json", "w") as f:
#         json.dump(location, f)
    
#     return {"status", "Success"}

 



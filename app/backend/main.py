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
    allow_origins=["http://172.20.103.96:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/api/upload")
async def saveFile(content: UploadFile = File(...)):
    extension = (".png", ".jpg", ".jpeg", ".heic")
    try: 
        if not content.filename.lower().endswith(extension):
            return {"status": "Error: Only image files allowed"}
        fileName = content.filename
        filePath = os.path.join(UPLOAD_DIR, fileName)
        with open (filePath, 'wb') as file:
            file.write(await content.read())

        return {"status": "File Uploaded"}

    except Exception as e:
        return {"status": f"Error: {str(e)}"}

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
    result = getReturnPlastic("uploads/" + file, city, state, zipCode)




@app.get("/api/materialGet")
def callReturnFile(file, city, state, zipCode): 
    result = getReturnMaterial("uploads/" + file, city, state, zipCode)


# @app.get("/api/location")
# def serveLocation(location : dict):
#     with open("location.json", "w") as f:
#         json.dump(location, f)
    
#     return {"status", "Success"}

 



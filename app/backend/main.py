from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



app.add_middleware(


    CORSMiddleware,


    allow_origins=["http://localhost:3000"],  # React app origin


    allow_credentials=True,


    allow_methods=["*"],


    allow_headers=["*"],


)


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def saveFile(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".png"):
        raise HTTPException(status_code=400, detail="Only PNG files allowed")

    fileName : str = file.filename

    filePath = os.path.join(UPLOAD_DIR, fileName)

    with open(filePath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return{"message": "Success"}


@app.get("/files/{fileName}")
def servePNG(fileName: str):
    filePath = os.path.join(UPLOAD_DIR, fileName)

    if not os.path.exists(filePath):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(filePath, media_type = "image/png")
 


# For file picker


@app.get("/api/get/listDIR/{DIR:path}")


#def listDirectory(DIR):



@app.get("/api/get/listDIR/{DIR:str}")

def location(latitude: int, longitude: int, postal: int):
    return{"message" : "Success"}

def root():
    return {"message" : "Hello World"}

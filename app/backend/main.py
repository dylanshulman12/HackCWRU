@@ -0,0 +1,19 @@





app = FastAPI()





app.add_middleware(


    CORSMiddleware,


    allow_origins=["http://localhost:3000"],  # React app origin


    allow_credentials=True,


    allow_methods=["*"],


    allow_headers=["*"],


)


 


# For file picker


@app.get("/api/get/listDIR/{DIR:path}")


def listDirectory(DIR):


 


    


 



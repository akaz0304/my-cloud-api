from fastapi import FastAPI
app=FastAPI(title="My Cloud API")

@app.get("/")
def read_root():
    return{
        "status": "Success",
        "message": "Welcome to my Cloud-Native API! It is working perfectly."
    }

@app.get("/health")
def health_check():
    return{
        "status":"Active",
        "version":"1.0",
        "server":"Ubuntu Docker Container"
    }
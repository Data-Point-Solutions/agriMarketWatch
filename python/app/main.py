from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to agriMarketWatch API"}

@app.get("/status")
def read_status():
    return {"status": "API is up and running"}
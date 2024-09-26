from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get('/v1/')
def home():
    return "Welcome User"
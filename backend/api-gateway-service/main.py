from fastapi import FastAPI


app: FastAPI = FastAPI()

@app.get("/")
def home():
    return "Welcome to the Expense Management Tool!"
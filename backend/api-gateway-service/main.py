from fastapi import FastAPI
from slowapi.middleware import SlowAPIASGIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
import socket


limiter: Limiter = Limiter(key_func=lambda request: request.client.host)

# print(f"Client Host: {socket.gethostname()}")

app: FastAPI = FastAPI()

app.middleware(SlowAPIASGIMiddleware)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/")
def home():
    return "Welcome to the Expense Management Tool!"
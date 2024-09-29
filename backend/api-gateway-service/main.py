from fastapi import FastAPI
from slowapi.middleware import SlowAPIASGIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from routes.user_service_proxy import setup_routes
from environment_manager import EnvironmentManager

# print(f"Client Host: {socket.gethostname()}")
limiter: Limiter = Limiter(key_func=lambda request: request.client.host)

app: FastAPI = FastAPI()

# Add SlowAPI middleware for rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIASGIMiddleware)

# setup_routes(app=app)
env_manager = EnvironmentManager(app)
env_manager.setup_routes()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/")
def home():
    return "Welcome to the Expense Management Tool!"
from fastapi import FastAPI
from slowapi.middleware import SlowAPIASGIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from routes.user_service_proxy import setup_routes
from environment_manager import EnvironmentManager
from fastapi.middleware.cors import CORSMiddleware
from secure import Secure

# print(f"Client Host: {socket.gethostname()}")
limiter: Limiter = Limiter(key_func=lambda request: request.client.host)

app: FastAPI = FastAPI()

# Initialize Secure instance
secure = Secure(
    content_security_policy="default-src 'self'",
    hsts=True,
    hsts_include_subdomains=True,
    hsts_preload=True,
    referrer="no-referrer",
    x_content_type_options=True,
    x_dns_prefetch_control=False,
    x_frame_options="DENY",
    x_xss_protection=1
)


# Add SlowAPI middleware for rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIASGIMiddleware)

@app.middleware("http")
async def set_secure_headers(request, call_next):
    response = await call_next(request)
    # Add security headers using the secure package
    secure.framework.fastapi(response)
    return response

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify allowed domains here (e.g., ['https://example.com'])
    allow_credentials=True,
    allow_methods=["*"],  # HTTP methods like 'GET', 'POST', etc. (or '*' for all)
    allow_headers=["*"],  # Allowed headers (or '*' for all)
)

# setup_routes(app=app)
env_manager = EnvironmentManager(app)
env_manager.setup_routes()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/")
def home():
    return "Welcome to the Expense Management Tool!"
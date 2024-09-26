from fastapi import FastAPI
from slowapi.middleware import SlowAPIASGIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from aiocache import caches, cached


limiter: Limiter = Limiter(key_func=lambda request: request.client.host)

# Setup Redis Caching
caches.set_config({
        'default': {
        'cache': "aiocache.RedisCache",
        'endpoint': "redis",
        'port': 6379,
        'timeout': 10,
        'serializer': {
            'class': "aiocache.serializers.JsonSerializer"
        }
    }
})

# print(f"Client Host: {socket.gethostname()}")

app: FastAPI = FastAPI()

app.middleware(SlowAPIASGIMiddleware)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

@limiter.limit("5/minute")  # 5 requests per minute rate limit
@cached(ttl=60)  # Cache response for 60 seconds
@app.get("/v1/")
def home():
    return "Welcome to the Expense Management Tool!"
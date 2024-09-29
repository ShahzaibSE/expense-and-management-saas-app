import requests
from fastapi import APIRouter, FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from aiocache import cached,caches

limiter: Limiter = Limiter(key_func=get_remote_address)

router = APIRouter()

# Setup Redis Caching
# caches.set_config({
#         'default': {
#         'cache': "aiocache.RedisCache",
#         'endpoint': "redis",
#         'port': 6379,
#         'timeout': 10,
#         'serializer': {
#             'class': "aiocache.serializers.JsonSerializer"
#         }
#     }
# })

@router.get("/user/v1/{path:path}")
@limiter.limit("2/minute")  # 5 requests per minute rate limit
@cached(ttl=60)  # Cache response for 60 seconds
def user_home(request:Request):
    return "Welcome User!"

def setup_routes(app:FastAPI):
    app.include_router(router)



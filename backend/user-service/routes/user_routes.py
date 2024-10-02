import requests
from fastapi import APIRouter, FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from aiocache import cached,caches

limiter: Limiter = Limiter(key_func=get_remote_address)

userRoutes = APIRouter()

@userRoutes.get("/user/v1/profile")
@limiter.limit("2/minute")  # 5 requests per minute rate limit
@cached(ttl=60)  # Cache response for 60 seconds
def get_user(request:Request):
    return "Welcome User!"

@userRoutes.post("/user/v1/login")
@limiter.limit("2/minute")  # 5 requests per minute rate limit
@cached(ttl=60)  # Cache response for 60 seconds
def get_user(request:Request):
    return "Successfully Logged In"

@userRoutes.post("/user/v1/signup")
@limiter.limit("2/minute")  # 5 requests per minute rate limit
@cached(ttl=60)  # Cache response for 60 seconds
def get_user(request:Request):
    return "Successfully Logged In"


from fastapi import APIRouter
from app.api.endpoints import douyin_web

router = APIRouter()

# Douyin routers
router.include_router(douyin_web.router, prefix="/douyin/web", tags=["Douyin-Web-API"])

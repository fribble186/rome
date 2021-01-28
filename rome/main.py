# coding=utf-8
# 启动命令：uvicorn rome.main:app

from fastapi import FastAPI
from rome.routers import router
from MDdoc import views

app = FastAPI()
app.include_router(router, prefix="/api")

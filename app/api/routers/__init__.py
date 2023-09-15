from fastapi import FastAPI

from app.api.routers import cv


def include_routers(app: FastAPI):
    app.include_router(cv.router)

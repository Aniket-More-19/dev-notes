from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.note import (router as notes_router)
from app.config import settings


app = FastAPI(title='dev-notes backend', description='backend apis for dev-notes web application')

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(notes_router)
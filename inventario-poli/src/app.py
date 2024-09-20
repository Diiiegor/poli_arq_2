from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.routes import router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

#Modules includes
app.include_router(router)
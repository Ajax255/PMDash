from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
from fastapi.middleware.cors import CORSMiddleware

from routers import pmdash_router
from routers import project_router
from routers import task_router

load_dotenv(find_dotenv())

app = FastAPI(title="PMDash-API", version="0.1.0")

origins = [
    'http://localhost:5050',
    'http://ui:4040',
    '*'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(pmdash_router.router)
app.include_router(project_router.router)
app.include_router(task_router.router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import mongo

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

app.include_router(mongo.router)

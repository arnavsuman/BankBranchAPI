from fastapi import FastAPI
from . import models
from .database import engine
from .routers import bank

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bank API")
app.include_router(bank.router)

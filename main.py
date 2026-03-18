from fastapi import FastAPI 
from routers import homeroute
from routers import crud
from db.database import Base, engine
import db.database_models

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(crud.router)
app.include_router(homeroute.router)

from fastapi import FastAPI 
from routers import homeroute
from routers import crud

app = FastAPI()

app.include_router(crud.router)
app.include_router(homeroute.router)

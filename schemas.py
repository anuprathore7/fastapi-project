from pydantic import BaseModel

class Create_book(BaseModel):
    title: str
    author : str

class Update_book(BaseModel):
    title : str
    author : str

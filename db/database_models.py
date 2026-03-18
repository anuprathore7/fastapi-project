from db.database import Base
from sqlalchemy import Column, Integer, String , VARCHAR

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    author = Column(String(255))
    
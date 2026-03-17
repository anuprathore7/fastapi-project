from fastapi import APIRouter, HTTPException
from schemas import Create_book , Update_book

router = APIRouter(
    prefix="/book",
    tags= ["books"]
)

books = [
    {"id": 1, "title": "Book One", "author": "Author One"},
    {"id": 2, "title": "Book Two", "author": "Author Two"}, 
    
]

@router.get("/get" , summary="Get all books")
def get_books():
    return books 
     

@router.get("/get/{book_id}" , summary="Get a book by ID")
def get_a_book(book_id : int):
    for book in books:
        if book["id"] == book_id:
            return book
    else :
        raise HTTPException(status_code=404, detail="Book not found")
    
@router.post("/create_book", summary="Create a new book")
def create_book (req_book : Create_book):
    new_book = req_book.model_dump()
    books.append(new_book)
    return {"message": "Book created successfully", "book": new_book}


@router.put("/update/{book_id}" , summary="Update a book by ID")
def update_book(book_id : int , req_book : Create_book):
    for book in books:
        if book["id"] == book_id:
            book["title"] = req_book.title
            book["author"] = req_book.author
            return {"message": "Book updated successfully", "book": book}
    else :
        raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/delete/{book_id}" , summary="Delete a book by ID")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    else :
        raise HTTPException(status_code=404, detail="Book not found")
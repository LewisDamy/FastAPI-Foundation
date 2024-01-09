from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

# Book Object
class Book:
    id: int
    title: str
    author: str
    description: str
    publish_date: int
    rating: int

    def __init__(self, id, title, author, description, publish_date, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.publish_date = publish_date
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = Field(title='id is not needed')
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    publish_date: int = Field(gt=1899, lt=2024)
    rating: str = Field(gt=0, lt=6)
    
    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'Famous Author',
                'description': 'A new description of a book',
                'published_date': '2024-01-01',
                'rating': 5
            }
        }


BOOKS = [
    Book(1, 'Computer Science', 'John Doe', 'A comprehensive introduction to computer science', 2020, 4.5),
    Book(2, 'The Great Gatsby', 'F. Scott Fitzgerald', 'A classic novel set in the Jazz Age', 1925, 4.0),
    Book(3, 'To Kill a Mockingbird', 'Harper Lee', 'A powerful story addressing racial injustice', 1960, 4.8),
    Book(4, '1984', 'George Orwell', 'A dystopian novel portraying a totalitarian society', 1949, 4.7),
    Book(5, 'The Catcher in the Rye', 'J.D. Salinger', 'A coming-of-age novel', 1951, 4.2)
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == int(book_rating):
            books_to_return.append(book)
    return books_to_return

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(publish_date: int = Query(gt=1899, lt=2024)):
    books_to_return = []
    for book in BOOKS:
        if book.publish_date == int(publish_date):
            books_to_return.append(book)
    return books_to_return

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    # operator will pass the key/value from BookRequest() into the Book() constructor
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

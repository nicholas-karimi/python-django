# standard library imports
from datetime import date
from django.shortcuts import get_object_or_404

# 3rd party imports
from pydantic import BaseModel, UUID4
from ninja import NinjaAPI, Schema, ModelSchema
from typing import Optional

#  local imports
from .models import Book, Author

app =  NinjaAPI()


# author schema
class AuthorSchema(Schema):
    id: int
    name: str
    birthdate: date

# use modle schema
class AuthorListSchema(ModelSchema):
    class Meta:
        model = Author
        fields = '__all__'

class BookSchema(Schema):
    id: UUID4
    title: str
    description: str
    isbn: str
    author_id: int
    pub_date: date
    slug: str

class BookListSchema(ModelSchema):
    author: AuthorListSchema
    class Meta:
        model = Book
        fields = '__all__'

# Post a new book schema
class CreateBookSchema(Schema):
    title: str
    description: str
    author_id: int | None = None  # Optional -> return none if not provided
    isbn: str
    pub_date: date
    is_deleted: bool = False

class BookCreateSchema(ModelSchema):
    class Meta:
        model = Book
        fields = '__all__'

class BookPatchSchema(Schema):
    title: Optional[str] = None
    description: Optional[str] = None
    author_id: Optional[int] = None
    isbn: Optional[str] = None
    pub_date: Optional[date] = None
    is_deleted: Optional[bool] = None





# get a single book using the slug
@app.get('/books/{slug}', response=BookSchema)

def book_detail(request, slug: str):
    '''This endpoint returns a single book'''
    book = get_object_or_404(Book, slug=slug)
    return book

# get all books
@app.get('/books', response=list[BookListSchema])
def book_list(request):
    '''This endpoint returns a list of books'''
    books = Book.objects.all()
    return books


# create a book
@app.post('books/', response=BookSchema)
def create_book(request, payload: CreateBookSchema):
    '''This endpoint creates a new book'''
    book_data = payload.model_dump() # model_dump() -> converts pydantic model to a python dict.
    book = Book.objects.create(**book_data)
    print(f"Book data: {book}")
    return book


# get authors
@app.get('authors/', response=list[AuthorSchema])
def author_list(request):
    '''This endpoint returns a list of authors'''
    authors = Author.objects.all()
    return authors


@app.delete('/books/{slug}')
def delete_book(request, slug: str):
    '''This endpoint deletes a book'''
    book = get_object_or_404(Book, slug=slug)
    book.delete()
    return {"success": True, "message": "Book deleted successfully"}


# update a book
@app.patch('books/{slug}', response=BookSchema)
def update_book(request, slug: str, payload: BookPatchSchema):
    '''This endpoint updates a book'''
    book = get_object_or_404(Book, slug=slug)
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(book, key, value)
    book.save()
    return {"success": True, "message": "Item updated successfully!"}
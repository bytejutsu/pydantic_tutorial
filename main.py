from db.session import db, connection
from db.models.book import book as book_tab
from schemas.book import Book
import json


def read_json():
    # read file
    with open('books.json', 'r') as myfile:
        data = myfile.read()
    # parse file
    obj = json.loads(data)
    return obj


def main():
    obj = read_json()
    book_list = obj["books"]
    for book in book_list:
        my_book = Book(**book)
        print(my_book.title)
        query = db.insert(book_tab).values(id=my_book.id, title=my_book.title, subtitle=my_book.subtitle, author=my_book.author)
        ResultProxy = connection.execute(query)


if __name__ == "__main__":
    main()

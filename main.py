import os
import json

LIBRARY_FILE = 'library.json'

class Library:
    def __init__(self, book):
        self.book = book
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(LIBRARY_FILE):
            with open(LIBRARY_FILE, 'r') as file:
                self.books = json.load(file)

    def set_book(self):
        if os.path.exists(LIBRARY_FILE):
            for dictionary in self.books:
                if self.book in dictionary['name']:
                    return False
            id = dictionary['id'] + 1
            book = {'id': id, 'name': self.book}
            self.books.append(book)
            self.set_file()
        else:
            book = {'id': 1, 'name': self.book}
            self.books.append(book)
            self.set_file()

    def set_file(self):
        with open(LIBRARY_FILE, 'w') as file:
            json.dump(self.books, file)


def main():
    while True:
        book = input('Book: ')
        user = Library(book)
        user.set_book()
        leave = input('Leave [Y/N]: ').upper()
        if leave == 'Y':
            break
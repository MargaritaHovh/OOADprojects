import datetime

class BookRegistration:
    books = []
    def __init__(self, title, author, genre, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = availability


    def add_book(self, book):
        BookRegistration.books.append(book)

    def available_books(self):
        for book in BookRegistration.books:
            print(book.title)

class MemberRegistration:
    def __init__(self, name, contact, borrowed_books):
        self.name = name
        self.contact = contact
        self.borrowed_books = borrowed_books

class LibraryManagementSystem:
    def borrow_book(self, member, book):
        print(f"{member.name} borrowed {book.title}")
        BookRegistration.books.remove(book)
        book.availability = "None"

    def returning_book(self, member, book):
        print(f"{member.name} returned {book.title}")
        BookRegistration.books.append(book)
        book.availability = "Available"

    def overdue_reports(self, book, member):
        report = f"The {member.name}'s {book.title} is overdue for 14 days"
        print(report)

        filename = f"{book.title}_{datetime.date.today().month}.txt"
        with open(filename, "w") as f:
            f.write(report)

    def search_book(self, attribute):
        if attribute.lower() == "title":
            for book in BookRegistration.books:
                print(book.title)
        elif attribute.lower() == "author":
            for book in BookRegistration.books:
                print(book.author)
        elif attribute.lower() == "genre":
            for book in BookRegistration.books:
                print(book.genre)
    

book1 = BookRegistration("Title1", "author1", "genre1", "Available")
book2 = BookRegistration("Title2", "author2", "genre2", "Available")
book3 = BookRegistration("Title3", "author3", "genre3", "Available")
book1.add_book(book1)
book2.add_book(book2)
book3.add_book(book3)

book3.available_books()

member1 = MemberRegistration("Ana", "Phone", None)

libmensys = LibraryManagementSystem()
libmensys.borrow_book(member1, book2)
print(book2.availability)

libmensys.returning_book(member1, book2)
print(book2.availability)

libmensys.overdue_reports( book1, member1)

libmensys.search_book("title")

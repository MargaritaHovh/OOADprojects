class Book:
    def __init__(self, title, author, genre, price, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity

class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.history = ""



class BookstoreSystem:
    def __init__(self):
        self.books = []
        self.shopping_cart = []
        self.cost = 0
  
    def book_registr(self, book):
        self.books.append(book)

    def add_books(self, book, customer):
        if book.quantity>=1:
            self.shopping_cart.append(book)
            self.books.remove(book)

            book.quantity -=1 


            customer.history = f"{customer.name} buy the {book.title}"
            print(customer.history)
        else:
            print("The book you are searching is not here")

    def remove_books(self, book, customer):
        for i in self.shopping_cart:
            if book in self.shopping_cart:
                self.shopping_cart.remove(book)
                self.books.append(book)
                book.quantity += 1

                customer.history = f"{customer.name} remove the {book.title}"
                print(customer.history)
            else:
                print("You haven't thatt book in youre card")



    def total_cost(self):
        for i in self.shopping_cart:
            self.cost += i.price
        print(self.cost)

    def save_history(self, customer):
        filename = "file.txt"
        with open(filename, "w") as f:
            f.write(f"{self.cost} \n")
            for book in self.shopping_cart:
                f.write(f"{customer.name} bought {book.title}\n")



book1 = Book("Title1", "author1", "genre1", 500, 4)
book2 = Book("Title2", "author2", "genre2", 100, 3)
book3 = Book("Title3", "author3", "genre3", 1500, 1)
book4 = Book("Title4", "author4", "genre4", 200, 6)

customer1 = Customer("Name1", "Phone")

system = BookstoreSystem()
system.book_registr(book1)
system.book_registr(book2)
system.book_registr(book3)
system.book_registr(book4)

system.add_books(book1,customer1)
system.add_books(book2,customer1)
system.add_books(book3,customer1)
system.add_books(book3,customer1)

system.total_cost()

system.save_history(customer1 )
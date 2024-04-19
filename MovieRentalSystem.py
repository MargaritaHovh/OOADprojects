from abc import ABC, abstractmethod

class Movie(ABC):
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    @abstractmethod
    def movie_type(self):
        pass
    

class Comedy(Movie):
    def movie_type(self):
        print("Movie is comedy")

class Drama(Movie):
    def movie_type(self):
        print("Movie is drama")

class RentalSystem(ABC):
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie.title)
    
    def search_movie(self):
        print(self.movies)


    @abstractmethod
    def rent_movie(self):
        pass

    @abstractmethod
    def return_movie(self):
        pass 
class RentalSystemImpl(RentalSystem):
    def rent_movie(self):
        print("print")
    def return_movie(self):
        print("d")

class Customer:
    def __init__(self, name, info):
        self.name = name
        self.info = info
    
class Rental:
    def __init__(self, customer, movie, rental_duration):
        self.customer = customer
        self.movie = movie
        self.rental_duration = rental_duration

    def rental_history(self):
        print(f"The rental history - {self.customer.name} rented {self.movie.title} for {self.rental_duration} days.")

comedy1 = Comedy("Comedy1", "comedy", 5)
comedy2 = Comedy("Comedy2", "comedy", 4)
drama1 = Drama("Drama1", "drama", 4 )
customer1 = Customer("Customer1", "Mail")
rental1 = Rental(customer1, comedy1, 7)
rental1.rental_history()

rental_system = RentalSystemImpl()
rental_system.add_movie(comedy1)
rental_system.add_movie(comedy2)
rental_system.add_movie(drama1)


rental_system.search_movie()









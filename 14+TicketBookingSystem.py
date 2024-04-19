
class Movie:
    def __init__(self, title, duration, rating, showtimes, available_seats):
        self.title = title
        self.duration = duration
        self.rating = rating
        self.showtimes = showtimes
        self.available_seats = available_seats

class User:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact


class BookingSystem:
    def __init__(self):
        self.movies = []
        self.tickets = []

    def movie_reg(self, movie):
        self.movies.append(movie)



    def book_ticket(self, movie_title):
        for i in self.movies:
            if i.title.lower() == movie_title.lower() and i.available_seats>=1:
                ticket = f"You booked ticket, {i.showtimes}, {i.available_seats}"
                self.tickets.append(ticket)
                i.available_seats -=1
                print(ticket)

                return
            
        ticket = f"We don't have that movie"
        print(ticket)


    
    def movie_report(self):
        with open("movie.txt", "w") as file:
            for ticket in self.tickets:
                file.write(ticket + "\n")


    
movie1 = Movie("Title1", 90, 5, "19:00", 5)
movie2 = Movie("Title2", 80, 4.5, "20:00", 2)
movie3 = Movie("Title3", 70, 5, "18:00", 12)

sys = BookingSystem()

sys.movie_reg(movie1)
sys.movie_reg(movie2)
sys.movie_reg(movie3)
sys.book_ticket("Title1")
sys.book_ticket("Title2")
sys.book_ticket("Title2")
sys.book_ticket("Title2")

sys.movie_report()

class Flight:
    def __init__(self, number, origin, destination, departure_date, available_seats):
        self.number = number
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.available_seats = available_seats


class User:
    def __init__(self, name, info):
        self.name = name
        self.info = info 


class AirlineSystem:
    def __init__(self):
        self.flights = []
        self.ticket = ""

    def flight_reg(self, flight):
        self.flights.append(flight)

    def search_flight(self, flight,  criteria):
        if criteria == "origin" and flight.available_seats>=1:
            print(f"{flight.origin}, You booked seat")
            self.ticket = "Flight detalis"
            print(self.ticket)
            flight.available_seats -=1

        elif criteria == "destination" and flight.available_seats>=1:
            print("{flight.destination}, You booked seat")
            self.ticket = "Flight detalis"
            flight.available_seats -=1

        elif criteria == "departure_date" and flight.available_seats>=1:
            print(f"{flight.departure_date}, You booked seat")
            self.ticket = "Flight detalis"
            flight.available_seats -=1

        else:
            raise TypeError("TE")


    def save_ticket(self):
        file = open("file.txt", "w")
        file.write(self.ticket)
        file.close()




sys = AirlineSystem()
flight1 = Flight(10, "origin1", "dest1", 15, 3)
sys.flight_reg(flight1)

sys.search_flight(flight1, "origin")

sys.save_ticket()
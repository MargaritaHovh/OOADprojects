class Taxi:
    def __init__(self, number, driver_name, availability, clas): 
        self.number = number
        self.driver_name = driver_name
        self.availability = availability
        self.clas = clas


class User:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class TaxiBookingSystem:
    def __init__(self):
        self.service = []
        self.fare = 0

    def taxi_reg(self, taxi):
        self.service.append(taxi)

    def book_taxi(self, taxi):
        if taxi.availability == "Available":
            order = f"{user.name} book taxi {taxi.number}"
            print(order)
            taxi.availability = "Not available"
        elif taxi.availability == "Not available":
            print("Taxi is not available")
        else:
            raise TypeError("type error")

    def fare_for_ride(self, distance, car ):
        if car.clas == "start":
            self.fare = distance * 10

        elif car.clas == "comfort":
            self.fare = distance * 18

        elif car.clas == "business":
            self.fare = distance * 30

        else:
            raise TypeError("type error")
        
    def save_bills(self):

        file = open("file.txt", "w")
        file.write(str(self.fare))
        file.close()

user = User("Name", "123")
taxi1 = Taxi(1, "Name", "Available", "start")
taxi2 = Taxi(2, "Name", "Available", "comfort")
taxi3 = Taxi(3, "Name", "Available", "business")

sys = TaxiBookingSystem()

sys.taxi_reg(taxi1)
sys.taxi_reg(taxi2)
sys.taxi_reg(taxi3)

sys.book_taxi(taxi1)
sys.book_taxi(taxi1)

sys.fare_for_ride(10, taxi1)
print(sys.fare)

sys.save_bills()

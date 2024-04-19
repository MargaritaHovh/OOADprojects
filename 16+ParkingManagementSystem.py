class Parking:
    def __init__(self, number, size, availability, duration):
        self.number = number
        self.size = size
        self.availability = availability
        self.duration = duration


class User:
    def __init__(self, name, vehicle_size):
        self.name = name
        self.vehicle_size = vehicle_size



class ParkingSystem:
    def __init__(self):
        self.parkings = []
        self.fee = 0
        self.parking = ""
        self.count = 0
        

    def parking_registration(self, parking):
        self.parkings.append(parking)

    def reserve_parking_space(self, space):
        if space.availability == "Available":
            self.parking = f"You reserved {space.number}th parking space"
            self.count +=1
            space.availability == "Not available"
            print(self.parking)

    def parking_fee(self, parking_space):
        if parking_space.size == "compact":
            self.fee = 5 * parking_space.duration
            print(self.fee)
        elif parking_space.size == "regular":
            self.fee = 10 * parking_space.duration
            print(self.fee)

        elif parking_space.size == "large":
            self.fee = 20 * parking_space.duration
            print(self.fee)
        else:
            raise TypeError("type error")

    def receipt_generation(self):
        print(f"The fee is {self.fee}, parking detalis are: {self.parking}")

    def save_report(self):
        file = open("parking.txt", "w")
        file.write(f"Count: {self.count}")
        file.close()


parking1 = Parking(5, "compact", "Available", 6)
parking2 = Parking(5, "regular", "Available", 3)
parking3 = Parking(5, "large", "Available", 6)
system = ParkingSystem()
system.reserve_parking_space(parking1)
system.reserve_parking_space(parking2)


system.parking_fee(parking1)
system.receipt_generation()

system.save_report()
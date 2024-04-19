from abc import ABC, abstractmethod
class Room:
    def __init__(self, number, type, status):
        self.number = number
        self.type = type
        self.status = status
    
class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.cust_rooms = []
        self.sum = 0
        self.booked = " "
        self.bill = " "

    
class ReservationSystem(ABC):
    @abstractmethod
    def room_registr(self):
        pass


class ReservationSystemImpl(ReservationSystem):
    def __init__(self):
        self.rooms = []
        self.customers = []

    def room_registr(self, room):
        self.rooms.append(room.number)

    def customer_registr(self, customer):
        self.customers.append(customer.name)

    def book_room(self, customer, room, type):
        if room.status:
            if type.lower() == room.type:
                customer.booked = f"{customer.name} booked {room.type} room"
                print(customer.booked)
                customer.cust_rooms.append(room)
                room.status == False

    def bill_generation(self, customer):
        for i in customer.cust_rooms:
            if i.type.lower() == "single":
                customer.sum +=10
            elif i.type.lower() == "double":
                customer.sum +=20
            elif i.type.lower() == "suite":
                customer.sum +=30
            else:
                raise TypeError("type error")
        print(customer.sum)

    def save_bills(self, customer):

        filename = f"{customer.name}.txt"
        with open(filename, "w") as f:
            f.write(customer.booked)
            f.write("\n")
            f.write(str(customer.sum))


room1 = Room(10, "single", True)
room2 = Room(11, "double", True)

customer1 = Customer("Maga", "Phone")
reserv_syst_impl = ReservationSystemImpl()

reserv_syst_impl.book_room(customer1, room1, "single")
reserv_syst_impl.book_room(customer1, room2, "double")

reserv_syst_impl.bill_generation(customer1)
reserv_syst_impl.save_bills(customer1)
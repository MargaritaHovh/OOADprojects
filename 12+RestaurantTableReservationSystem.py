import datetime

class Table:
    def __init__(self, number, capacity, availability):
        self.number = number
        self.capacity = capacity
        self.availability = availability

class User:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class ReservationSystem:
    def __init__(self):
        self.report = ""

    def book_table(self,user, table):
        if table.availability == "Available":
            self.report = f"{user.name} ordered that table"
            print(self.report)
            table.availability = "Not available"

        elif table.availability == "Not available":
            print("The table is taken")

        else:
            raise TypeError("type error")

    def generate_report(self):
        file = open("file.txt", "w")
        file.write(self.report)
        file.write(f"Date: {datetime.datetime.now()}")
        file.close()



user1 = User("Name1", "contact")
table8 = Table(8, 3, "Available")
sys = ReservationSystem()

sys.book_table(user1, table8)
sys.book_table(user1, table8)

sys.generate_report()
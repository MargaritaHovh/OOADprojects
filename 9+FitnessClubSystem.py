from abc import ABC, abstractmethod
import datetime

class Member:
    def __init__(self, name, contact, membership_level):
        self.name = name
        self.contact = contact
        self.membership_level = membership_level


class MembershipLevel(ABC):
    @abstractmethod
    def level_type(self):
        pass

class Standard(MembershipLevel):
    def __init__(self):
        self.name = "Standard"
        self.fitness_area = 12
        self.massage = 1
        self.pool = 6
        self.days = 30

    def level_type(self):
        print("Standart")

class Premium(MembershipLevel):
    def __init__(self):
        self.name = "Premium"
        self.fitness_area = 24
        self.massage = 2
        self.pool = 12
        self.days = 30

    def level_type(self):
        print("Premium")

class AllIncluded(MembershipLevel):
    def __init__(self, fitness_area, massage, pool):
        self.name = "All included"
        self.fitness_area = fitness_area
        self.massage = massage
        self.pool = pool
        self.days = 30

    def level_type(self):
        print("AllIncluded")


class System:
    def __init__(self):
        self.histories = []
        self.fee = 0
        self.members = []

    def reg_member(self, member):
        self.members.append(member)

    def monthly_fee(self, membership_level):
        if membership_level.name == "Standard":
            self.fee = 1500
        elif membership_level.name == "Premium":
            self.fee = 2500
        elif membership_level.name == "All included":
            self.fee = 4000
        else:
            raise TypeError("We don't have that membership level")

    def enter_area(self, user, level, area):
        if area.lower() == "fitness" and level.fitness_area >= 1:
            level.fitness_area -=1
            history = f"{user.name} entered to fitness at {datetime.date.today()}"
            self.histories.append(history)

        elif area.lower() == "massage" and level.massage >= 1:
            level.massage -=1
            history = f"{user.name} entered to massage at {datetime.date.today()}"
            self.histories.append(history)

        elif area.lower() == "pool" and  level.pool >= 1:
            level.pool -=1
            history = f"{user.name} entered to pool at {datetime.date.today()}"
            self.histories.append(history)

        else:
            raise TypeError("Type error")

    def monthly_statistics(self):
        for i in self.histories:
            print(i)

    def upgrade_downgrade(self, member):
        new_level = input("Enter the new membership level: ")

        if new_level.lower() == "standard":
            member.membership_level = Standard()
        elif new_level.lower() == "premium":
            member.membership_level = Premium()
        elif new_level.lower() == "all included":
            member.membership_level = AllIncluded()
        else:
            raise ValueError("Invalid membership level")

        print(f"{member.name}'s membership level has been updated to {new_level}")

    def save_monthly_bill(self):
        filename = "file.txt"
        with open(filename, "w") as f:
            f.write(f"The monthly bill is {self.fee}")
            


standard = Standard()
member1 = Member("Mem1", "123456789", standard)

system = System()


system.enter_area(member1, standard, "fitness")
system.enter_area(member1, standard, "massage")

system.monthly_statistics()

system.monthly_fee(standard)
system.save_monthly_bill()

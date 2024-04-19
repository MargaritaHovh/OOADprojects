class TravelPackage:
    def __init__(self, destination, price, available_slots):
        self.destination = destination
        self.price = price
        self.available_slots = available_slots

class User:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class TravelBookingSystem:
    def __init__(self):
        self.packages = []
        self.tickets = []

    def package_registration(self, package):
        self.packages.append(package)

    def search_package_by_price(self, price, slot):
        for package in self.packages:
            if package.price == price and package.available_slots == slot and package.available_slots>=1: 
                ticket = f"You booked slot in {price} price and at {slot} slot, the destination is {package.destination}"
                print(ticket)
                package.available_slots -= 1
                self.tickets.append(ticket)
                return
            
        print("We dont have")

    def save_report(self):
        file = open("package.txt", "w")
        for ticket in self.tickets:
            file.write(ticket + "\n")
        file.close()

package1 = TravelPackage("dest1", 500, 3)
package2 = TravelPackage("dest2", 3000, 1)

user1 = User("Name", "contact")
system = TravelBookingSystem()

system.package_registration(package1)
system.package_registration(package2)

system.search_package_by_price(500,3)
system.search_package_by_price(3000,1)
system.search_package_by_price(3000,1)

system.save_report()
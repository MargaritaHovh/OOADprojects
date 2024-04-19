from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def car_type(self):
        pass

class Inventory(ABC):
    @abstractmethod
    def car_inventory(self):
        pass

class ElectricCar(Car):
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def car_type(self):
        print("This is electric car")

class HybridCar(Car):
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def car_type(self):
        print("This is hybrid car")

class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def show_cars(self, search_car):
        search_car.display_available_cars()
    def buy_car(self, car):
        print(f"{self.name} bought {car.make}")   

class SalesPeople(Inventory):
    def __init__(self, name, commission_rate):
        self.name = name
        self.commission_rate = commission_rate
        

    def sales_history(self, car):
        print(f"{car.make} sold out")
        
    def car_inventory(self):
        print("Car inventory")


class SearchCar:
    def __init__(self, *cars):
        self.cars = list(cars)

    def display_available_cars(self):
        print("Available cars: ")
        for car in self.cars:
            print(car.make)

electric_car1 = ElectricCar("Tesla", "Model", 80000)
hybrid_car1 = HybridCar("Toyota", "Model", 80000)
search_car = SearchCar(electric_car1, hybrid_car1)
search_car.display_available_cars()
customer1 = Customer("Ana", "Phone5")
customer1.buy_car(electric_car1)
salesperson1 = SalesPeople("Aram", 0.05)
salesperson1.sales_history(electric_car1)

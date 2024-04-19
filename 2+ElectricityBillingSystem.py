from abc import ABC, abstractmethod
import datetime

class BillingSystem(ABC):
    @abstractmethod
    def customer_registration(self, customer):
        pass

    @abstractmethod
    def electricity_consumption(self):
        pass

    @abstractmethod
    def bill_calculation(self):
        pass

    @abstractmethod
    def bill_generation(self):
        pass
    
    @abstractmethod
    def bill_saving(self):
        pass


class Customer:
    def __init__(self, name, contact, meter_number):
        self.name = name
        self.contact = contact
        self.meter_number = meter_number
        self.electricity_consumption = 0 
        self.bill_calc = 0 

class BillingSystemImpl(BillingSystem):
    def __init__(self):
        self.customers = []

    def customer_registration(self, customer):
        self.customers.append(customer)

    def electricity_consumption(self, customer):
        customer.electricity_consumption = input("input of electricity consumption for a given period for a customer: ")
        
    def bill_calculation(self, customer):
        customer.bill_calc = int(customer.electricity_consumption) * 10
        print(customer.bill_calc)

    def bill_generation(self, customer):
        customer.generation = f"The electricity consumption: {customer.electricity_consumption} \nTotal amount: {customer.bill_calc}"
        print(customer.generation)
    
    def bill_saving(self, customer):
        filename = f"{customer.name}_{datetime.date.today()}.txt"
        with open (filename, "w") as file:
            file.write(f"Total amount {customer.generation}")



customer = Customer("Name", "Phone", 123)

billing_system = BillingSystemImpl()
billing_system.customer_registration(customer)
billing_system.electricity_consumption(customer)
billing_system.bill_calculation(customer)
billing_system.bill_generation(customer)

billing_system.bill_saving(customer)

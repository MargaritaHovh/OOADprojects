import datetime
from abc import ABC, abstractmethod
class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.report = ""

class InteractionTypes(ABC):
    @abstractmethod
    def interaction_type(self):
        pass

class Sale(InteractionTypes):
    def __init__(self, date, user, amount, warrant_period):
        self.date = date
        self.user = user
        self.amount = amount
        self.warrant_period = warrant_period
        print(f"We give sale for {user.name}, amount is {amount} and warrant peroid is {warrant_period} days") 

    def interaction_type(self):
        print("Sale")

class WarrantyService(InteractionTypes):
    def __init__(self, sale, user, service_cost):
        self.sale = sale
        self.user = user
        self.service_cost = service_cost
        print(f"We have warranty service for {user.name}, {sale.warrant_period},  service cost is {service_cost}")

    def interaction_type(self):
        print("Warranty service")

class Compliant(InteractionTypes):
    def __init__(self, sale, user, compliant_description):
        self.sale = sale
        self.compliant_description = compliant_description

        print(f"The {user.name} didn't have any compliant")

    def interaction_type(self):
        print("Compliant")
    
    
class CustomerRelationshipManagement:
    def report_generation(self, customer, sale, warranty_service, compliant):
        customer.report = f"Customer personal detalis: {customer.name}, {customer.contact},\n Interaction history: Sale - {sale.amount}  Waarranty service - {warranty_service.service_cost}  Compaliant - {compliant.compliant_description} "
        print(customer.report)


    def report_saving(self, customer):
        filename = f"{customer.name}_{datetime.date.today().month}.txt"
        with open(filename, "w") as f:
            f.write(customer.report)



customer1 = Customer("Cust1", "Phone")
sale = Sale(10, customer1, 1500, 7 )
warranty_service = WarrantyService(sale, customer1, 500)
compliant = Compliant(sale, customer1, None)

cust_rel_manag= CustomerRelationshipManagement()

cust_rel_manag.report_generation(customer1, sale, warranty_service, compliant)
cust_rel_manag.report_saving(customer1)
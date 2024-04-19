class Delivery:
    def __init__(self, item, origin, destination, time):
        self.item = item
        self.origin = origin
        self.destination = destination
        self.time = time
        self.status = 1
                                                 
class User:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

                                                                       
class LogisticsSystem:
    def __init__(self):
        self.deliveries = []

    def deliveryRegister(self, deliver):
        self.deliveries.append(deliver)

    def updateStatus(self, delivery):
        if delivery.status < 3:
            delivery.status += 1

    def trackDelivery(self, delivery):
        if delivery.status == 1:
            print('24')
        elif delivery.status == 2:
            print('6')
        elif delivery.status == 3:
            print('done')
    
    def manageDeliveries(self):
        for delivery in self.deliveries:
            if delivery.status == 2:
                print(f'Delivery of {delivery.item} accelerated')
                delivery.status += 1

d1 = Delivery('item1', 'origin1', 'dest1', 24)
d2 = Delivery('item2', 'origin2', 'dest2', 23)
ls = LogisticsSystem()
ls.deliveryRegister(d1)
ls.deliveryRegister(d2)

ls.updateStatus(d1)
ls.trackDelivery(d1)

ls.updateStatus(d1)
ls.updateStatus(d2)

ls.trackDelivery(d1)
ls.manageDeliveries()
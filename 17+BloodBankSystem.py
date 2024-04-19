class Donor:
    def __init__(self, name, contact_info, blood_type):
        self.name = name
        self.contact_info = contact_info
        self.blood_type = blood_type

class BloodType:
    def __init__(self, type, count):
        self.type = type
        self.count = count


class BloodBankSystem:
    def __init__(self):
        self.bloods = []
        self.str = ""

    def blood_bank(self, blood):
        self.bloods.append(blood)


    def increment_unit(self, blood_type):
        blood_type.count+=1
    
    def decrement_unit(self, blood_type):
        blood_type.count-=1

    def utilize_blood(self, blood_type):
        if blood_type.count >=1:
            print("You can utilize it")
            blood_type.count -=1

    def search_blood_type(self, blood_type ):
            for blood in self.bloods:
                if blood.type == blood_type:
                    self.str = "We have that blood type, you can use it"
                    print(self.str)
                    return
                
            print("We dont have that blood type")

    def generate_reports(self):
        for count in self.bloods:
            if count.count <=1:
                print(f"{count.type} is low")
            else:
                print(f"{count.type} is high")

    def save_reports(self):
        file = open("blood.txt", "w")
        file.write(self.str)
        file.close()


sys = BloodBankSystem()
blood1 = BloodType("Positive", 0)
blood2 = BloodType("Negative", 5)
sys.blood_bank(blood1)
sys.blood_bank(blood2)


donor1 = Donor("Name", "contact", blood1)

sys.increment_unit(blood1)
print(blood1.count)

sys.search_blood_type("Positive")


sys.generate_reports()
sys.save_reports()









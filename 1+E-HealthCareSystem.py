from abc import ABC, abstractmethod
import datetime

class Doctor:
    def __init__(self, name, specialization, experience, contact):
        self.name = name 
        self.specialization = specialization
        self.experience = experience
        self.contact = contact
    
class Patient:
    def __init__(self, name, birth_date, gender, contact, medical_condition):
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.contact = contact
        self.medical_condition = medical_condition
        self.medical_history = []

    
class HealtManagementSystem(ABC):
    def __init__(self):
        self.patients = []
        self.doctors = []
    
    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.patients.append(doctor)
        

    @abstractmethod
    def add_medical_history(self):
        pass

    @abstractmethod
    def report_generation(self):
        pass

class HealtManagementSystemImpl(HealtManagementSystem):
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.report = ""
    def add_medical_history(self, patient, diagnos, treatment, medication):
        record = {
            "date": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "diagnos": diagnos,
            "treatment": treatment,
            "medication": medication}
        patient.medical_history.append(record)
        
    def report_generation(self, patient):
        
        personal_detalis = f"Patient's personal detalis: Name - {patient.name}, Date of birth - {patient.birth_date}, Gender - {patient.gender}, Contact - {patient.contact}, Medical condition - {patient.medical_condition} \n Patient's medical history: {patient.medical_history}"

        self.report = personal_detalis

        print(self.report)
    
    def save_report(self, patient):

        filename = f"{patient.name}_{datetime.datetime.now()}.txt"

        with open(filename, "w") as file:
            file.write(self.report)


    
patient1 = Patient("Name1", 2000, "Female", "Phone", "MedCond" )

hmsi1 = HealtManagementSystemImpl()
hmsi1.add_medical_history(patient1, "diagnos1", "treatments", "medications")
hmsi1.report_generation(patient1)
hmsi1.save_report(patient1)


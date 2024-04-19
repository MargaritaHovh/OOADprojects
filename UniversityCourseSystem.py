from abc import ABC, abstractmethod

class Assignment(ABC):
    @abstractmethod
    def complete_assignment(self):
        pass

class Student(Assignment):
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def complete_assignment(self):
        print("Complete assignment")
        
    def view_progress(self):
        print("View progress")

class Professor:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.courses = []

    def create_course(self, course):
        self.courses.append(course)
        print(f"The course {course.name} was created")
    
    def delete_course(self, course):
        self.courses.remove(course)
        print(f"The {course.name} was deleted")

class Course(ABC):
    def __init__(self, name, instructor):
        self.name = name
        self.instructor = instructor
        self.content = None

    @abstractmethod
    def enroll(self):
        pass

class UndergraduateCourse(Course):
    def enroll(self, student):
        print(f"{student.name} enrolled in Undergraduate course")


class GraduateCourse(Course):
    def enroll(self, student):
        print(f"{student.name} enrolled in Graduate course")

student1 = Student("Student1", "Phone")
student2 = Student("Student1", "Mail")
professor1 = Professor("Professor1","Phone")
undergraduate_course = UndergraduateCourse("Undergraduate", "Instructor")
graduate_course = GraduateCourse("Graduate", "Instructor")
undergraduate_course.enroll(student1)
professor1.create_course(graduate_course)
professor1.delete_course(graduate_course)






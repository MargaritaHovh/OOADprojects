from abc import ABC, abstractmethod

class Posting(ABC):
    @abstractmethod
    def job_type(self):
        pass


class JobSearchPlatform(ABC):
    @abstractmethod
    def search_job(self):
        pass
    
    def apply_job(self):
        print("You applied to this job")

    @abstractmethod
    def manage_job_posting(self):
        pass
    @abstractmethod
    def review_applications(self):
        pass

class Staff(JobSearchPlatform):
    def __init__(self):
        self.jobs = []

    def search_job(self):
        print(self.jobs)

    def add_job(self, job):
        self.jobs.append(job.title)

    def manage_job_posting(self, job):
        self.jobs.remove(job.title)


    def review_applications(self, company, seeker):
        a = company.applications(seeker.resume)
        if a:
            print(f"{company.name} hired {seeker.name}")
        else:
            print("Rejected")


class FullTimeJob(Posting):
    def __init__(self, title, description, salary):
        self.title = title 
        self.description = description
        self.salary = salary

    def job_type(self):
        print("Full time job")

class PartTimeJob(Posting):
    def __init__(self, title, description, salary):
        self.title = title 
        self.description = description
        self.salary = salary

    def job_type(self):
        print("Part time job")
        

class Company:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def applications(self, resume):
        if resume is None:
            return False
        else:
            return True
        
class Seeker:  
    def __init__(self, name, contact_info, resume):
        self.name = name
        self.contact_info = contact_info
        self.resume = resume

    

fulltimejob1 = FullTimeJob("JobF", "fulltime", 1500)
fulltimejob2 = FullTimeJob("JobF", "fulltime", 2500)
parttimejob1 = PartTimeJob("JobP", "parttime", 1000)
parttimejob2 = PartTimeJob("JobP", "parttime", 900)



staff = Staff()
staff.add_job(fulltimejob1)
staff.add_job(fulltimejob2)
staff.add_job(parttimejob1)
staff.add_job(parttimejob2)

staff.search_job()
staff.manage_job_posting(parttimejob2)
staff.search_job()

seeker1 = Seeker("Maga", "Mail", "Resume1")
company = Company("Comp", "Phone")

staff.review_applications(company, seeker1)
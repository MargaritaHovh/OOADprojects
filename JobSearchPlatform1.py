from abc import ABC, abstractmethod

class Posting(ABC):
    @abstractmethod
    def job_type(self):
        pass

class JobPostingFactory:
    @staticmethod
    def create_job_posting(job_type, title, description, salary):
        if job_type == "FullTime":
            return FullTimeJob(title, description, salary)
        elif job_type == "PartTime":
            return PartTimeJob(title, description, salary)
        else:
            raise ValueError("Invalid job type")

class FullTimeJob(Posting):
    def __init__(self,title, description, salary):
        self.title = title
        self.description = description
        self.salary = salary

    def job_type(self):
        print("Full-time")

class PartTimeJob(Posting):
    def __init__(self,title, description, salary):
        self.title = title
        self.description = description
        self.salary = salary
    
    def job_type(self):
        print("Part-time")

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
    
    def add_job(self, job):
        self.jobs.append(job.title)

    def search_job(self):
        print(self.jobs)
    

    def manage_job_posting(self,job):
        self.jobs.remove(job.title)

    def review_applications(self, company, seeker):
        a = company.applications(seeker.resume)
        if a:
            print(f"{company.name} hired {seeker.name}")
        else:
            print("Rejected")     


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
    def __init__(self, name ,contact_info, resume):
        self.name = name
        self.contact_info = contact_info
        self.resume = resume

jobfactory = JobPostingFactory()

fulltimejob1 = jobfactory.create_job_posting("FullTime", "JobF", "fulltime", 1500)
fulltimejob2 = jobfactory.create_job_posting("FullTime", "JobF", "fulltime", 2500)

parttimejob1 = jobfactory.create_job_posting("PartTime", "JobP", "parttime", 1000)
parttimejob2 = jobfactory.create_job_posting("PartTime", "JobP", "parttime", 900)

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

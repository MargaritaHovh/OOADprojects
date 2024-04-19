class Job:
    def __init__(self, title, description, requirements, salary, company, availability):
        self.title = title
        self.description = description
        self.requirements = requirements
        self.salary = salary
        self.company = company
        self.availability = availability

class User:
    def __init__(self, name, contact, resume):
        self.name = name
        self.contact = contact
        self.resume = resume


class JobPortalSystem:
    def __init__(self):
        self.jobs = []

    def job_reg(self, job):
        self.jobs.append(job)

    def search_job(self, user, job):
        if (user.resume == job.requirements) and (job.availability == "Available"):
            print(f"{user.name} applied to this job")
            job.availability = "Not available"
        else:
            print("You can't apply to this job")

    def send_notifications(self, user):
        for job in self.jobs:
            if job.requirements == user.resume:
                print(f"Notification: This job - {job.requirements} match to you")




job1 = Job("Title1", "Python", "python developer", 1500, "picsart", "Available")
job2 = Job("Title2", "CPP", "CPP developer", 1500, "picsart", "Available")

user1 = User("Name1", "phone", "python developer")
user2 = User("Name1", "phone", "CPP developer")
sys = JobPortalSystem()
sys.search_job(user1, job1)
sys.search_job(user1, job1)

sys.job_reg(job1)
sys.job_reg(job2)
sys.send_notifications(user2)




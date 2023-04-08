class Employee():

    workinghours=10   

    def __init__(self,name,salary,job):

        self.name=name
        self.salary=salary
        self.job=job
    workinghours=12  
    def printdetails(self):
        return f"name is {self.name}, salary is {self.salary} and the job{self.job}"
  
    
    @classmethod
    def changeworkinghours(cls,newworkinghours):
        cls.workinghours=newworkinghours

obj1=Employee("Nanthu",5000,"police")
obj2=Employee("sara",10000,"software")

obj1.changeworkinghours(45)
print(obj1.workinghours)
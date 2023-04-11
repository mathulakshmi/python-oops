



class Student:
  
    fees = 10000
    no_of_stu = 0

    def __init__(self, name, rollno, dob, city):
        self.name=name
        self.dob=dob
        self.rollno=rollno
        self.dob=dob
        self.city=city
       
    @staticmethod
    def department(dept):
        available_dept =['eee','csc']
        if dept in available_dept:
            return True
        return False

stu1 = Student('raja',100,1998,"chennai")
stu2 = Student('sara',200,2001,"chennai")
       
print(stu1.department('cvil'))
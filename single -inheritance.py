# class surya:


#     def Actor(self):
#         print("Acting")

#     def sing(self):
#         print("singing")

# class karthik(surya):
#     def dancer(self):
#         print("dancing")

#     def writer(self):
#         print("writer")

# obj1=karthik()
# obj1.Actor()
                           


# #single inheritance

# class Employee():
#     workinghours=10
#     def __init__(self,name,salary,degree):
#         self.name=name
#         self.salary=salary
#         self.dgree=degree
#     workinghours=12
    
#     def printdetails(self):
#         return f"name is {self.name}, salary is {self.salary}, and the degree is{self.dgree}"
    
#     @classmethod
#     def changeworkinghours(cls,newworkinghours):
#         cls.workinghours=newworkinghours

 

# obj1=Employee("Mathu",3000,"B.E")
# obj2=Employee("AAA",4500,"ME")



# class programmer(Employee):
#     pass
 

# obj3=programmer("Raja",80000,"programmer")

# print(obj3.printdetails())






class Employee:
    
    def __init__(self,name,salary,degree):
        self.name=name
        self.salary=salary
        self.degree=degree
    
    
    def printdetails(self):
        return f"name is {self.name}, salary is {self.salary}, and the degree is{self.degree}"
    
    @classmethod
    def changeworkinghours(cls,newworkinghours):
        cls.workinghours=newworkinghours


obj1=Employee("Mathu",3000,"B.E")
obj2=Employee("AAA",4500,"ME")



class programmer(Employee):
   
    def __init__(self,name,salary,degree,language):
        self.name=name
        self.salary=salary
        self.degree=degree
        self.language=language

    def printprog(self) :
       return f"name is {self.name}, salary is {self.salary}, and the degree is{self.degree}, language is{self.language}"
           
 

obj3=programmer("Raja",80000,"programmer",["python"])

print(obj3.printdetails())
print(obj3.printprog())
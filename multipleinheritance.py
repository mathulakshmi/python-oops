class Employee():
    var=1
    def __init__(self,name,salary,degree):
        self.name=name
        self.salary=salary
        self.degree=degree
    
    
    def printdetails(self):
        return f"name is {self.name}, salary is {self.salary}, and the degree is{self.degree}"
    
obj1=Employee("Mathu",3000,"B.E")
obj2=Employee("AAA",4500,"ME")


class player:
    var=2
    no_of_games=4
    def __init__(self,aname,agame):
        self.name=aname
        self.game=agame
        
oops1 = player("Ram","cricket")

class coolprogrammer(Employee,player):
 pass

oops2=coolprogrammer("saranya",56000,"BE")
print(oops2.printdetails())
print(oops2.var)
# def func1():
#     print("welcome!")
    
# func2=func1
# del func1
# func2()


def tec1(func):
    def execution():
        print("Executing")
        func()
        print("executed")  
    return execution
@tec1

def Mathu():
    print("welcome to sankarankovil")
Mathu()          



# app=tec1(Mathu)
# app()
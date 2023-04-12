numbers=["33","45","1","2","3"]
print(type(numbers[0]))
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])
print(type(numbers[0]))
    ######## 
numbers=["33","45","1","2","3"]
numbers=list(map(int,numbers))
print(type(numbers[4]))
    ######## 
def square(a):
    return a*a
num=[1,2,3,4,5,6,7,8,9,10]
for i in num:
    print(i)
num=list(map(square,num))
for i in num:
    print(i)
    ######## 
num=[1,2,3,4,5,6,7,8,9,10]
for i in num:
    print(i)
num=list(map(lambda a: a*a,num))
for i in num:
    print(i)
    ######## 
def isgreaterthan5(num):
    return num>5
list1=[1,2,3,4,5,6,7,8,9,]  
list1=list(filter(isgreaterthan5,list1)) 
print(list1)     
    ########
from functools import reduce
list1=[1,2,3,4]
num=0
for i in list1:
    num=num+i
print(num)
    ########
from functools import reduce
list1=[1,2,3,4]
num=reduce(lambda x,y:x+y,list1)
# num=reduce(lambda x,y:x*y,list1)
print(num)
def simplegeneratorfun() :
    a=11
    b=2
    c=a+b
    yield a 
    yield b 
    yield c
x = simplegeneratorfun()    

print(next(x))
print(next(x))


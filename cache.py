# caching
import time
import functools       #least recently used cache

@functools.lru_cache(maxsize=2)
def some_work(n):
    print("calculating")
    time.sleep(2)
    return n*100

if __name__=="__main__":
    var1=some_work(2)
    print(var1)
    var2=some_work(3)
    print(var2)
    var3=some_work(2)
    print(var3)
    var4=some_work(4)
    print(var1)
    var5=some_work(5)
    print(var5)
    var6=some_work(6)
    print(var6)
    var7=some_work(7)
    print(var7)
    var8=some_work(8)
    print(var8)
    var9=some_work(9)
    print(var9)
    var10=some_work(2)
    print(var10)
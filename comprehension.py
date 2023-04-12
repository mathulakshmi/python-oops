# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)        

ls=[i for i in range(100) if i%3==0]
print(ls)

# # dictionary
dict1={i:f"item{i}"for i in range(100)}
dict1={value:key for key,value in dict1.items()}
print(dict1)

# generator
evens=(i for i in range(101) if i%2==0)
# print(evens.__next__())
# print(evens.__next__())
for i in evens:
     print(i)
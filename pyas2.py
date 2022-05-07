"""DICTIONARY"""
dict={"name":"aishwarya","age":17,"course":"B.E"}
print(dict)
print(dict["age"])
print(len(dict))
print(type(dict))

x=dict.get("course")
print(x)

x=dict.keys()
dict["age"]=18
print(x)

x=dict.values()
print(x)

dict={"name":"aishwarya","age":17,"course":"B.E"}
x=dict.items()
dict["age"]=18
print(x)

if "course" in dict:
    print("yes,'course' is there")

dict.update({"course":"B.Tech"})

dict.pop("age")
print(dict)

dict={"name":"aishwarya","age":17,"course":"B.E"}
dict.popitem()
print(dict)

dict={"name":"aishwarya","age":17,"course":"B.E"}
del dict["course"]
print(dict)

dict.clear()
print(dict)

dict={"name":"aishwarya","age":17,"course":"B.E"}
for name in dict:
    print(dict[name])
for name in dict.keys():
    print (name)

mydict=dict.copy()
print(mydict)

"""CALCULATOR"""
a=input("enter number 1:")
b=input("enter number 2:")
a=int(a)
b=int(b)
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
s=input("enter operation to perform:")

if s=='1':
    r=a+b
    print("sum is",r)
elif s=='2':
    r=a-b
    print("difference is",r)
elif s=='3':
    r=a*b
    print("product is",r)
elif s=='4':
    r=a/b
    print("quotient is",r)

name=input("enter name:")
age=input("enter your age:")
print("your name is", name, "and you are", age ,"years old")



"""string functions"""
txt="hello world"
x=txt.capitalize()
print(x)
x=txt.casefold()
print(x)
x=txt.center(50)
print(x)
txt="hello hi hello"
x=txt.count("hello")
print(x)
x=txt.encode()
print(x)
x=txt.endswith(".")
print(x)
txt="h\te\tl\tl\to"
x=txt.expandtabs(3)
print(x)
x=("welcome to the college")
x=txt.find("college")
print(x)
txt="this costs only {price:.2f} rupees"
x=txt.format(price=54.8)
print(x)
x=txt.index("only")
print(x)
txt="hi004"
x=txt.isalnum()
print(x)
x=txt.isalpha()
print(x)
x=txt.isascii()
print(x)
x=txt.isdecimal()
print(x)
x=txt.isdigit()
print(x)
x=txt.isidentifier()
print(x)
x=txt.islower()
print(x)
x=txt.isnumeric()
print(x)
x=txt.isprintable()
print(x)
x=txt.isspace()
print(x)
x=txt.istitle()
print(x)
x=txt.isupper()
print(x)
tuple=("apple","banana","orange")
x="&".join(tuple)
print(x)
txt="hello"
x=txt.ljust(15)
print(x)
txt="HEllO"
x=txt.lower()
print(x)
txt="    hi "
x=txt.lstrip()
print(x)
txt="hello"
x=txt.maketrans("h","y")
print(txt.translate(x))
txt="hello hi welcome"
x=txt.partition("hi")
print(x)
x=txt.replace("welcome","bye")
print(x)
x=txt.rfind("hi")
print(x)
x=txt.rindex("hi")
print(x)
x=txt.rjust(20)
print(x)
txt="i ate apple and it is my favorite"
x=txt.rpartition("and")
print(x)
txt="hello hi welcome"
x=txt.rsplit(", ")
print(x)
txt="  welcome   "
x=txt.rstrip()
print(x)
txt="come to the class"
x=txt.split()
print(x)
txt="welcome to the inauguration\nbye"
x=txt.splitlines()
print(x)
x=txt.startswith("welcome")
print(x)
txt="  hello    "
x=txt.strip()
print(x)
x=txt.swapcase()
print(x)
txt="welcome to the house"
x=txt.title()
print(x)
x=txt.upper()
print(x)
txt="35"
x=txt.zfill(20)
print(x)



"""list functions"""
fruits=['apple','banana','orange']
fruits.append("mango")
print(fruits)
x=fruits.copy()
print(x)
x=fruits.count("apple")
print(x)
veg=['potato','tomato','greens']
fruits.extend(veg)
print(fruits)
fruits=['apple','banana','orange','mango']
x=fruits.index("banana")
print(x)
fruits.insert(1,"pineapple")
print(fruits)
fruits.pop(2)
print(fruits)
fruits.remove("mango")
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.clear()
print(fruits)

"""AREA OF CIRCLE"""
radius=input("enter radius:")
radius=int(radius)
area=3.14*radius**2
print("area of circle is",area)


"""EXTENSION OF FILE"""
import os
split_tup=os.path.splitext('name.py')
ext=split_tup[1]
print("file extension is",ext)

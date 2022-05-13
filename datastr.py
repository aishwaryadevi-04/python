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

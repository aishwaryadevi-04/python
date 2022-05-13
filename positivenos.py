#  Print positive numbers from a list
list = []
n = int(input("enter the number of elements:"))
for i in range(1, n + 1):
    value = int(input(" enter %dst element : "%i))
    list.append(value)
print("the list is",list)
print("positive Numbers in this List are : ")
for j in range(n):
    if(list[j] >= 0):
        print(list[j])

#Printing positive numbers as a list
list1 = []
list2=[]
n = int(input("enter the number of elements:"))
for i in range(1, n + 1):
    value = int(input("enter %dst element : "%i))
    list1.append(value)
print("the list is",list1)
print("positive Numbers in this List are : ")
for j in range(n):
    if(list1[j] >= 0):
        list2.append(list1[j])
print(list2)

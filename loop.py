#fibonacci sequence
n = int(input("enter no of terms in fibonacci sequence:"))
n1, n2 = 0, 1
count = 0
if n <= 0:
   print("enter a positive integer")
elif n== 1:
   print("Fibonacci sequence is:",n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       next= n1 + n2
       n1 = n2
       n2 = next
       count += 1

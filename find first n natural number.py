# Python Program to find Sum of N Natural Numbers
  
number = int(input("Please Enter any Number: "))
 
total = 0
i= 1
 
while (i <= number):
    total = total + i
    i =i+ 1
 
print("The Sum of Natural Numbers from 1 to",number,"=",total)

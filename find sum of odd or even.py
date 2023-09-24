# Python Program to find Sum of Even and Odd Numbers from 1 to N
 
number = int(input(" Please Enter the Maximum Value : "))
even= 0
odd= 0
 
for i in range(1, number+ 1):
    if(i % 2 == 0):
        even = even +i
    else:
        odd= odd+i
 
print("The Sum of Even Numbers from 1 to",number,"=",even)
print("The Sum of Odd Numbers from 1 to ",number,"=",odd)

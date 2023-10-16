# Write a program to take number from user and do calculation based on user given arithmatic operaton.
import math
n1 = float(input("Enter the number 1 : "))
n2 = float(input("Enter the number 2 : "))
op = input("Enter the operation to perform : ")
addition = n1+n2
subtraction = n1-n2
multiplication = n1*n2
division = n1/n2


if op == 'addition' or op == '+':
 
 print("The addition of the number "+str(n1)+ " and "+str(n2)+" is : ",float(addition))

elif op == 'subtraction' or op == '-':
 
 print("The subtraction of the number "+str(n1)+" from "+str(n2)+" is : ",float(subtraction))

elif op == 'multiplication' or op == '*':
  
  print("The multiplication of the number "+str(n1)+" and "+str(n2)+" is : ",float(multiplication))

elif op == 'division' or op == '/':
   
   print("The division of the number "+str(n1)+" from "+str(n2)+" is : ",float(division))

else:
  
  print("Hey Buddy! You Should Enter Valid Arithmatic Operator's Name Or Symbol")
  
  


 

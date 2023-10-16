#write a program that prints calender for a given month and year.

import calendar
Y = int(input("Enter the Year: "))
M = int(input("Enter the Month: "))
print(calendar.month(Y,M))
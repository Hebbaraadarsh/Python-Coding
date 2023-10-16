# Write a program to take two date of birth and time in the right format and display the difference b/w them in the years months and days hour,minutes and seconds format.

from datetime import datetime

# Input from the user
date_str1 = input("Enter the first date (DD/MM/YYYY HH:MM:SS): ")
date_str2 = input("Enter the second date (DD/MM/YYYY HH:MM:SS): ")

# Convert the input strings to datetime objects
try:
    date1 = datetime.strptime(date_str1, "%d/%m/%Y %H:%M:%S ") 
    date2 = datetime.strptime(date_str2, "%d/%m/%Y %H:%M:%S ")

    # Calculate the difference
    timedelta = date2 - date1

    # Extract years, months, days, hours, minutes, and seconds
    years = timedelta.days // 365
    months = (timedelta.days % 365) // 30
    days = (timedelta.days % 365) % 30
    hours, remainder = divmod(timedelta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Display the result
    #Method 1 :
    print(f"Difference: {years} years, {months} months, {days} days,{hours} hours, {minutes} minutes, {seconds} seconds ")
    
    #Method 2 :
    #print(f"Difference: {years}/{months}/{days} and {hours}:{minutes}:{seconds}")
    

except ValueError:
    print("Invalid date format. Please use 'DD/MM/YYYY HH:MM:SS' format.")

# program to take two date of birth and display the difference b/w them in  days.

from datetime import datetime

# Function to calculate the difference between two dates
def date_difference(date1, date2):
    try:
        date_format = "%d/%m/%Y"  # Define the date format
        date1_obj = datetime.strptime(date1, date_format)
        date2_obj = datetime.strptime(date2, date_format)
        delta = abs(date2_obj - date1_obj)
        return delta.days  # Return the difference in days
    except ValueError:
        return "Invalid date format. Please use DD/MM/YYYY format."

# Get input from the user
date_str1 = input("Enter the first date (DD/MM/YYYY): ")
date_str2 = input("Enter the second date (DD/MM/YYYY): ")

# Calculate the difference between the two dates
difference = date_difference(date_str1, date_str2)

# Display the result
if isinstance(difference, int):
    print(f"The difference between the two dates is {difference} days.")
else:
    print(difference)
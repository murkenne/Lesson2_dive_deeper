# Write a Python program that prompts the user to input a year

# Prompt the user to input a year
year = int(input("Enter a year: "))

# Determine if the year is a leap year
if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


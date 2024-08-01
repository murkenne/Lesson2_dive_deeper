# Task Write a python program that asks the user to enter three numbers
# Your code should then identify and print out the largest number among the three

# Ask user to input the numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number"))

# Find the largest number

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Task 2 determine the smallest number amongst the 3  

 # Determine the smallest number
 
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

# Print the largest and smallest numbers
print("The largest number is:", largest)
print("The smallest number is:", smallest)   

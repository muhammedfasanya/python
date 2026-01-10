#Boolean operations are the backbone of logic in Python.
#They allow your code to make decisions by evaluating whether statements are True or False.

#Comparison Operator Cheat Sheet
#When working with these exercises, 
# you'll frequently use these operators to generate your True or False values:
# = 10
#==	Equal to	x == 10 → True
#!=	Not equal to	x != 5 → True
#>	Greater than	x > 5 → True
#<	Less than	x < 20 → True
#>=	Greater than or equal to	x >= 10 → True
#<=	Less than or equal to	x <= 15 → True
#%	Modulo (Remainder)	x % 3 == 1 → True

#LOGICAL OPERATORS
#Logical operators help you combine multiple boolean expressions to form more complex conditions.
#Here are the primary logical operators you'll use:
#and	Logical AND	(x > 5) and (x < 15) → True
#or	Logical OR	(x < 5) or (x > 15) → False
#not	Logical NOT	not(x == 10) → False
#Exercise 1: Check if 25 is greater than 10 and less than 30
#Solution:
#result1 = (25 > 10) and (25 < 30)
#print(result1)  # Output: True
#Exercise 2: Verify if 15 is equal to 15 or 20
#Solution:
#result2 = (15 == 15) or (15 == 20)
#print(result2)  # Output: True
#Exercise 3: Determine if 8 is not equal to 10
#Solution:
#result3 = not(8 == 10)
#print(result3)  # Output: True
#Exercise 4: Check if 50 is less than or equal to 60 and greater than 40
#Solution:
#result4 = (50 <= 60) and (50 > 40)
#print(result4)  # Output: True

#FINAL EXAMPLE
#The "Lucky Number" Validator
#You are writing logic for a digital lottery.
# A number is considered "Lucky" only if it passes a specific set of tests.

#number = 42

# Check individual conditions
#is_even = (number % 2 == 0)
#is_in_range = (10 <= number <= 50)
#is_not_forbidden = (number != 13 and number != 21)

# Combine them using boolean operators
#is_lucky = is_even and is_in_range and is_not_forbidden

#print(f"Is {number} a lucky number? {is_lucky}")



#Output: Is 42 a lucky number? True#In this example, the number 42 is evaluated against three conditions:
# it must be even, within the range of 10 to 50, and not equal to 13 or 21.
# If it meets all these criteria, it is deemed "Lucky".



#ASSIGNMENT: Boolean Operations in Python
#For the examples above,Set your own individual conditions, then Combine them using boolean operators
# Wrrite a python code for each of these, to determine if it is a lucky number and include the output
# ASSIGNMENT: Boolean Operations in Python
# Lucky Number Checker (Custom Conditions)


number = 36
is_even = (number % 2 == 0)              # number must be even
is_multiple_of_3 = (number % 3 == 0)     # number must be divisible by 3
is_in_range = (20 <= number <= 60)       # number must be between 20 and 60
is_not_forbidden = (number != 30)        # number must not be 30


is_lucky = is_even and is_multiple_of_3 and is_in_range and is_not_forbidden

# Output result  
print(f"Is {number} a lucky number? {is_lucky}")
#Is 36 a lucky number? True







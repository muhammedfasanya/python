# More on input functions in Python, including explanations and examples of using .split() for multiple inputs:
# Learning how to use the input() function is a fundamental step in making your Python programs interactive. By default, input() always returns data as a string, so you’ll often need to "cast" (convert) that data into integers or floats for calculations.

# Example1. Get User Name: Write a Python program to get a user's name as input and print a greeting message.

# name = input("Enter your name: ")
# print("Hello, " + name + "!")


#Example2 Add Two Numbers: Write a Python program to get two numbers as input and print their sum.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("Sum:", num1 + num2)


# Example3. Get Multiple Inputs: Write a Python program to get multiple values as input and print them.

# values = input("Enter multiple values separated by spaces: ").split()
# print("You entered:", values)


# Using `.split()` for Multiple InputsThe .split() method splits a string into a list of substrings based on a specified separator (default is whitespace).

# Example4:

# input_str = "apple banana orange"
# fruits = input_str.split()  # ['apple', 'banana', 'orange']


#Example5 You can specify a custom separator:

# input_str = "apple,banana,orange"
# fruits = input_str.split(',')  # ['apple', 'banana', 'orange']


# Example6. `.split()`1. Get Multiple Numbers: Write a Python program to get multiple numbers as input and print their sum.

# numbers = input("Enter numbers separated by spaces: ").split()
# numbers = [int(num) for num in numbers]
# print("Sum:", sum(numbers))

#Example7. Get Name and Age: Write a Python program to get a user's name and age as input and print them.

# name, age = input("Enter your name and age separated by a space: ").split()
# age = int(age)
# print("Name:", name)
# print("Age:", age)

# Example8. Get User Details: Write a Python program to get a user's name, age, and city as input and print them.

# name, age, city = input("Enter your name, age, and city separated by commas: ").split(',')
# age = int(age)
# print("Name:", name)
# print("Age:", age)
# print("City:", city)


# Example9. Calculate Average: Write a Python program to get multiple numbers as input and calculate their average.

# numbers = input("Enter numbers separated by spaces: ").split()
# numbers = [float(num) for num in numbers]
# average = sum(numbers) / len(numbers)
# print("Average:", average)


# Example10. Get Scores and Calculate Grade: Write a Python program to get a student's scores in three subjects and calculate their average grade.

# scores = input("Enter scores in Math, Science, and English separated by spaces: ").split()
# scores = [float(score) for score in scores]
# average = sum(scores) / len(scores)
# print("Average Grade:", average)


# Using `.split()` with Different Separators- Comma-separated inputs: input_str.split(',')
# - Space-separated inputs: input_str.split() (default)
# - Custom separator: input_str.split(';')

#Example11. Comma-separated inputs: input_str.split(',')

# input_str = "apple,banana,orange"
# fruits = input_str.split(',')
# print(fruits)  # ['apple', 'banana', 'orange']


# Example12. Space-separated inputs: input_str.split() (default)

# input_str = "apple banana orange"
# fruits = input_str.split()
# print(fruits)  # ['apple', 'banana', 'orange']


# Example13. Custom separator: input_str.split(';')

# input_str = "apple;banana;orange"
# fruits = input_str.split(';')
# print(fruits)  # ['apple', 'banana', 'orange']


#Example14. Multiple character separator: input_str.split(', ')

# input_str = "apple, banana, orange"
# fruits = input_str.split(', ')
# print(fruits)  # ['apple', 'banana', 'orange']


#Example 15. Tab-separated inputs: input_str.split('\t')

# input_str = "apple\tbanana\torange"
# fruits = input_str.split('\t')
# print(fruits)  # ['apple', 'banana', 'orange']


# Example16. Split a string with a custom separator: Write a Python program to split the string "hello-world-python" using the '-' separator.

# input_str = "hello-world-python"
# words = input_str.split('-')
# print(words)  # ['hello', 'world', 'python']


# Example16. Split a string with multiple spaces: Write a Python program to split the string "apple   banana   orange" using space as the separator.

# input_str = "apple   banana   orange"
# fruits = input_str.split()
# print(fruits)  # ['apple', 'banana', 'orange']

# The Math Mapper
# Goal: Take two numbers at once from the user and add them together.

# The Problem: Since .split() returns a list of strings, you can't add them directly.

# The Solution: Use the map() function to convert all items in the list to integers simultaneously.

# Solution:

# Python

# # Example17: Add Two Numbers Using map() and .split()
# Input two numbers like: 10 20
# num1, num2 = map(int, input("Enter two numbers separated by a space: ").split())

# total = num1 + num2

# print(f"The sum of {num1} and {num2} is {total}.")
# Explanation of the Code:
# input("Enter two numbers separated by a space: ") prompts the user to enter two numbers
# Why use these?
# Efficiency: It’s much faster for a user to type "10 20 30" than to wait for three separate prompts.

# Data Handling: This is how data is often formatted in coding competitions and technical interviews.
# Key Tips to Remember
# Prompting: Always include a string inside the parentheses, like input("Type here: "), so the user knows what to do.

# Errors: If you try to do input() + 5 without converting to an int, Python will throw a TypeError.

# Leading/Trailing Spaces: Users often hit the spacebar by accident. You can use .strip() to clean it up: name = input("Name: ").strip().


# ASSIGNMENT
# Exercise 1: The Personalized Greeting
# Goal: Ask the user for their name and favorite color, then print a personalized message.

# The Task: Prompt the user for two separate inputs and combine them into one sentence.

# The Concept: Basic string input and concatenation.

# Solution:# Exercise 1: Personalized Greeting

name = input("Enter your name: ")
favorite_color = input("Enter your favorite color: ")

message = "Hello " + name + "! Your favorite color is " + favorite_color + "."

print(message)


# # Python



# # Output: Hello ****! It's cool that your favorite color is *****.

# Exercise 2: The Age Calculator
# Goal: Ask the user for their birth year and calculate how old they will be by the end of the current year (2026).

# The Task: Convert the input string into an integer to perform subtraction.

# The Concept: Type casting using int().

# Solution: Exercise 2: The Age Calculator

birth_year = input("Enter your birth year: ")

birth_year = int(birth_year)
current_year = 2026

age = current_year - birth_year

print("You will be", age, "years old by the end of 2026.")



# # Output: You will be ** years old by the end of 2026.


# Exercise 3: Area of a Rectangle (With Decimals)
# Goal: Create a program that asks for the length and width of a rectangle and calculates the area.

# The Task: Allow the user to enter decimal numbers (like 5.5).

# The Concept: Using float() for numerical precision.

# Solution:# Exercise 3: Area of a Rectangle (With Decimals)


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width


print("The total area of the rectangle is:", area)



#Output: The total area of the rectangle is: ***
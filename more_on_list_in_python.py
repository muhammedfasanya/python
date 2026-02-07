#MORE ON LIST IN PYTHON
# In Python, a list is one of the most versatile and frequently used data structures.
# Think of it as a container that holds a sequence of items in a specific order.

# #To understand lists, you should keep these four properties in mind:

# Ordered: Lists maintain the order in which elements are inserted.

# Mutable: You can change, add, or remove items after the list is created.

# Allows Duplicates: You can have multiple items with the same value.


# Heterogeneous: A single list can contain different data types (integers, strings, and even other lists).


# Creating a List
# Lists are defined by placing elements inside square brackets [], separated by commas.
# fruits = ["apple", "banana", "cherry"]
# mixed_list = [1, "Hello", 3.14, True]
# empty_list = []


# Accessing Elements (Indexing)
# Python uses zero-based indexing. You can also use negative indexing to count from the end of the list.
# list[0] is the first element.
# list[-1] is the last element.


# Slicing
# Slicing allows you to get a sub-section of a list using the syntax list[start:stop:step].
# numbers = [0, 1, 2, 3, 4, 5]
# print(numbers[1:4])  # Output: [1, 2, 3] (excludes index 4)


# Modifying Lists
# Because lists are mutable, you can update them in place:

# Method,Description,Example
# .append(x),Adds an item x to the end of the list.,ls.append(4)
# ".insert(i, x)",Inserts item x at position i.,"ls.insert(0, ""first"")"
# .extend(iterable),Appends all items from another list/tuple.,"ls.extend([5, 6])"
# .remove(x),Removes the first occurrence of value x.,"ls.remove(""apple"")"
# .pop(i),Removes and returns the item at index i.,val = ls.pop(1)
# .clear(),Removes all items from the list.,ls.clear()

# List Comprehension
# This is a concise, "Pythonic" way to create new lists based on existing ones. It is often faster and more readable than using a standard for loop.
# Syntax: [expression for item in iterable if condition]
# # Create a list of squares for even numbers only
# squares = [x**2 for x in range(10) if x % 2 == 0]
# # Output: [0, 4, 16, 36, 64]

# Common List Functions
# Function,Description,Example
# len(list),Returns the number of items in the list.,len(fruits)
# min(list),Returns the smallest item in the list.,min(numbers)
# max(list),Returns the largest item in the list.,max(numbers)
# sum(list),Returns the sum of all items in the list.,sum(numbers)
# Sorting Lists
# You can sort lists in place using the .sort() method or create a new sorted list using the sorted() function.
# numbers = [3, 1, 4, 1, 5]
# numbers.sort()  # In-place sort
# sorted_numbers = sorted(numbers)  # Returns a new sorted list
# Reversing Lists
# You can reverse the order of elements in a list using the .reverse() method.
# numbers = [1, 2, 3, 4, 5]
# numbers.reverse()  # Now numbers is [5, 4, 3, 2,1]


# ASSIGNMENT
# Exercise 1: Task: Print the first and last elements of a list.
# Solution:my_list = [10, 20, 30, 40, 50]
# # Output: First element: 10, Last element: 50

# Exercise 2: Task: Create a new list containing the squares of all even numbers from an existing list.
# Solution:numbers = [1, 2, 3, 4, 5, 6]

# squared_evens = []

# for num in numbers:
#     if num % 2 == 0:
#         squared_evens.append(num ** 2)
# print(squared_evens)
# Output: [4, 16, 36]

# Exerccise 3: Replace the second element in a list with 100.
# # Solution:numbers = [10, 20, 30, 40, 50]
# numbers[1] = 100
# print(numbers)
# Output: [10, 100, 30, 40, 50]

# Exerccise 3: Find the length of a list.
# solution:numbers = [10, 20, 30, 40, 50]
# length = len(numbers)
# print("The length of the list is:", length)
 # Output: The length of the list is: 5

# # Exercise 4: Sort a list of numbers in descending order.
# Solution:numbers = [12, 5, 67, 23, 34]
# numbers.sort(reverse=True)
# print(numbers)
# Output: [67, 34, 23, 12, 5]

# # Exercise 4: Sort a list of numbers in ascending order.
# # Solution:numbers = [34, 5, 67, 23, 12]
# numbers.sort()
# print(numbers)
 # Output: [5, 12, 23, 34, 67]

# # Exercise 5: Reverse a list of strings.
# # Solution:fruits = ['apple', 'banana', 'cherry']
# fruits.reverse()
# print(fruits)
# Output: ['cherry', 'banana', 'apple']

# # Excercise 6: Add 60 to the end and 15 at index 1.
 # Output: [10, 15, 20, 30, 40, 50, 60]

# # Exercise 7: Remove the first occurrence of 20 from the list.
# # Solution:numbers = [10, 20, 30, 20, 40]
# numbers.remove(20)
# print(numbers)
  # Output: [10, 30, 20, 40]

# # Exercise 8: Clear all elements from a list.
# # Solution:numbers = [10, 20, 30]
# numbers.clear()
# print(numbers)
 # Output: []

# Excercise 9: Remove duplicates from a list.
# Solution:numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_numbers = list(set(numbers))
# print(unique_numbers)
 # Output: [1, 2, 3, 4, 5] (order may vary)

# Excercise 10: Find the maximum and minimum values in a list.
# Solution:numbers = [2, 5, 7, 10, 3]
# print("Maximum:", max(numbers))
# print("Minimum:", min(numbers))
  # Output: Maximum: 10, Minimum: 2


# Exercise 11:Create a list of squares from 1 to 5.
# Solution:squares = [x**2 for x in range(1, 6)]
# print(squares)
  # Output: [1, 4, 9, 16, 25]

# Excercise 12 : Reverse a list without using reverse().
# Solution:numbers = [1, 2, 3, 4, 5]
# reversed_list = numbers[::-1]
# print(reversed_list)
#  # Output: [5, 4, 3, 2, 1]

# # Exercise 13:Check if 20 exists in the list.
# # Solution:numbers = [10, 20, 30, 40]
# exists = 20 in numbers
# print("20 exists in the list:", exists)
 # Output: 20 exists in the list: True

# # Exercise 14: Find the index of the first occurrence of 30 in the list.
# # Solution:numbers = [10, 20, 30, 40]
# index = numbers.index(30)
# print("The index of the first occurrence of 30 is:", index)
 # Output: The index of the first occurrence of 30 is: 2













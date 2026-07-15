# At AI2C we use Python for extraction, transformation, loading (SQL/NoSQL),
# exploration(Pandas) , modeling (AI) (SciKitLearn/Pytorch), Back end dev (Flask and FastAPI)

# Conditions are expressions that ALWAYS evaluate to a Boolean Value

# if condition:
#   # code
# elif condition:
#   # code
# else:
#   # code

# score = 89
# if score >= 90:
#    print("Grade: A")
# elif score >= 80:
#    print("Grade: B")
# elif score >= 70:
#   print("Grade: C")
# elif score >= 60:
#   print("Grade: D")
# else:
#   Print("Grade: F")

# You can place "if" or "elif"statements inside other "if" or "else" blocks to create more complex decision structures

# Practical exercise - Conditional Statements

# num = int(input("PLease choose a number?"))

# if num >= 1:
#    print("THe number is Positive")
# elif num == 0:
#    print("The number is Zero")
# else:
#   print("The number is Negative")

# Hands-on exercises

### Exercise 1: Check if a Number is Positive

# **Goal**: Write a Python Script that asks a user for an integer number, and then checks if the number is positive using an `if` statement.


# ✅ *Check*: Should print "The number is positive" if the number is greater than 0.

# user_num = float(input("Choose a number?"))

# if user_num > 0:
#     print("Positive")
# else:
#     print("This is not a positive number!")

# ### Exercise 2: Even or Odd

# **Goal**: Write a Python script that asks a user for an integer number.  Check if the number is even or odd using `if` and `else`.


# ✅ *Check*: Should print "Even" or "Odd" based on the number.

# user_num = int(input("Choose a number?"))

# if user_num % 2 == 0:
#     print("Positive")
# else:
#     print("Negative")

### Exercise 3: Age Category

# **Goal**: Write a python script that asks a user for their age, and then uses `if`, `elif`, and `else` to print the correct category for the person by based on their age.

# - Under 13: "Child"
# - 13-19: "Teenager"
# - 20-64: "Adult"
# - 65+: "Senior"


# ✅ *Check*: Should print the correct category based on age.

# user_age = int(input("What is your age?"))

# if user_age >= 65:
#     print("Senior")
# elif user_age >= 20:
#     print("Adult")
# elif user_age >= 13:
#     print("Teenager")
# else:
#     print("Child")

# ### Exercise 4: Compare Two Numbers

# num_1 = int(input("Pick your first number?"))
# num_2 = int(input("Pick your second number?"))

# if num_1 > num_2:
#     print(f"{num_1} is larger")
# elif num_1 == num_2:
#     print(f"{num_1} and {num_2} are equal")
# else:
#     print(f"{num_2} is larger")

# LOOPS
# if we want to run a defined number of iterations we use a FOR LOOP
# if we aren't running a defined number of iterartions we use WHILE LOOP
# an_example_list=[1,2,3,"Hello","Goodbye"]
# my_list = ["hello"]
# my_list.append("Goodbye")
# my_list.append(5)
# my_list.append(True)
# print(len(my_list)) this will return the length of the list


# range(stop) generates a sequence of numbers starting from 0 (defualt), up but not includes the stop value
# range(start, stop) dictates what number to include
# range(start, stop, step) the step condition tells it how many number to skip at a time

# 'for' loop_variable 'in' sequence
#   #code
# fruits = ['apples', 'banana', 'cherry']
# for fruit in fruits:
#   print(fruit)

# 'while' condition:
#   # block of code

# count = 0
# while count < 5:
#   print(count)
#   count += 1
# WHILE loops never end, you need to end the loop inside the while loop

# user_number = int(input("Select an even number"))
# while user_number % 2 == 1:
#     print("This is an odd number")
#     user_number = int(input("Select an even number"))
# else:
#     print("Thank you for picking an even number!")
# user_number = int(input("Select an even number"))
# while user_number % 2 == 1:
#     user_number = int(input("Select an even number"))
# print(f"Great job! you entered an even number, {user_number}")

# secret_number = 76

# user_guess = int(input("Guess a number: "))
# count = 1
# while user_guess != secret_number:
#     if user_guess < secret_number:
#         print("Your guess was low")
#     else:
#         print("Your guess was high")
#     user_guess = int(input("Guess a number: "))
#     count += 1
# print(f"Congratulations, you guessed correct. The secret number was {secret_number}")
# print(f"It took you {count} guesses")

# String length check
# user_qoute = input("What is your favorite qoute? ")

# if len(user_qoute) >= 10:
#     print("Long string")
# else:
#     print("Short string")

# Exercise 7: Logical AND Operator

# user_num = int(input("Please pick a number "))

# if user_num >= 10 and user_num <= 20:
#     print(f"{user_num} is in range")
# else:
#     print(f"{user_num} is out of range")

# Exercise 8: Logical OR Operator
# import string

# for letter in string.ascii_lowercase:
#     print(letter)

# letter = input("Pick a letter! ")

# if (
#     letter == "a"
#     or letter == "e"
#     or letter == "i"
#     or letter == "o"
#     or letter == "u"
#     or letter == "A"
#     or letter == "E"
#     or letter == "I"
#     or letter == "O"
#     or letter == "U"
# ):
#     print("Vowel")
# else:
#     print("Consonant")

# Exercise 9: Leap year Checker

# user_year = int(input("PLease pick a year. "))

# if user_year % 4 == 0 and (user_year % 100 != 0 or user_year % 400 == 0):

#     print("You picked a leap year, HAZAAAA!")
# else:
#     print("This year can't jump!!!!!")

# Exercise 10: Nested Conditionals - BMI Calculator

# user_wt = float(input("How much do you weigh(KG)? "))
# user_ht = float(input("How tall are you(meters)? "))

# bmi = user_wt / (user_ht**2)

# if bmi >= 30:
#     print("FATTY")
# elif bmi >= 25:
#     print("fatty")
# elif bmi >= 18.5:
#     print("Not fatty")
# else:
#     print("You need to eat more!")

# HANDS-On #2
# Exercise 11: create and print a list

# colors = ["red", "blue", "green"]
# for color in colors:
#     print(color)

# Exercise 12: list length

# numbers_list = list(range(5, 26, 5))
# print(f"This lsit has {len(numbers_list)} items!")

# Exercise 13: Append to a list

# my_list = []

# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append("four")
# my_list.append(5.0)

# print(my_list)

# Exercise 14: Loop through range

# numbers = range(1, 11)

# for number in numbers:
#     print(number)

# Exercise 15: Sum Numbers in a list

# numbers = [4, 7, 2, 9, 12]

# total = 0

# for number in numbers:
#     total += number

# print(total)

# Exercise 16: List membership

# available_fruits = ["apple", "banana", "orange", "mango"]

# fruit = input("What fruit do you want? ")

# if fruit in available_fruits:
#     print("!n stock!")
# else:
#     print("Not in stock.")

# Exercise 17: Count Even Numbers
# Goal: Count how many even numbers are in a list using a for loop.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ✅ Check: Should print "There are 5 even numbers".

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# count = 0

# for number in numbers:
#     if number % 2 == 0:
#         count += 1
# print(f"There are {count} even numbers")

# Exercise 18: While Loop Countdown
# Goal: Use a while loop to count down from 10 to 1.

# count = 10
# ✅ Check: Should print 10, 9, 8, ..., 2, 1.

# count = 10

# while count > 0:
#     print(count)
#     count -= 1
# How do I make this one line?

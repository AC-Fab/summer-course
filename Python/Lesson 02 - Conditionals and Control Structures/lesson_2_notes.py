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

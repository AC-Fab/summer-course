# num_list = list(range(1, 101))

# for number in num_list:
#     if number % 3 == 0 and number % 5 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("FizzBuzz")
#     else:
#         print(number)

# import random

# player_score = 0
# computer_score = 0

# print("Welcome to Rock, Paper, Scissors!")

# while True:

#     user_choice = input("Enter rock, paper, or scissors: ")
#     computer_choice = random.choice()
#     print(f"You chose: {user_choice}")
#     print(f"Computer chose: {computer_choice}")

#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (
#         (user_choice == "rock" and computer_choice == "scissors")
#         or (user_choice == "paper" and computer_choice == "rock")
#         or (user_choice == "scissors" and computer_choice == "paper")
#     ):
#         print("You win this round!")
#         player_score += 1
#     else:
#         print("Computer wins this round!")
#         computer_score += 1

#     print(f"Current Score -> You: {player_score} | Computer: {computer_score}")

# import random

# secret_num = random.randint(1, 100)
# user_choice = int(input("Select a number between 1 and 100. "))
# count = 1
# while user_choice != secret_num:
#     if user_choice > secret_num:
#         print("You guessed to high. \n Please guess again.")
#     else:
#         print("You guessed to low. \n Please guess again.")
#     user_choice = int(input("Select a number between 1 and 100. "))
#     count += 1
# print(f"Congrats you guessed the secret number in {count} tries")

# import random

# # Track scores across multiple rounds
# player_score = 0
# computer_score = 0

# print("Welcome to Rock, Paper, Scissors!")

# while True:
#     # 1. Get and clean user input
#     user_choice = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").strip().lower()

#     # Check if the player wants to end the game
#     if user_choice == "quit":
#         print("\nThanks for playing!")
#         print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
#         break

#     # Validate user choice
#     options = ["rock", "paper", "scissors"]
#     if user_choice not in options:
#         print("Invalid choice. Please try again.")
#         continue

#     # 2. Generate computer choice
#     computer_choice = random.choice(options)
#     print(f"You chose: {user_choice}")
#     print(f"Computer chose: {computer_choice}")

#     # 3. Determine the winner
#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (user_choice == "rock" and computer_choice == "scissors") or \
#          (user_choice == "paper" and computer_choice == "rock") or \
#          (user_choice == "scissors" and computer_choice == "paper"):
#         print("You win this round!")
#         player_score += 1
#     else:
#         print("Computer wins this round!")
#         computer_score += 1

#     # Display running score
#     print(f"Current Score -> You: {player_score} | Computer: {computer_score}")

# import random as rn

# number = rn.randint(0, 100)

# if number > 50:
#     print("The number is greater than 50!")
# elif number == 50:
#     print("The Number is 50!")
# else:
#     print("The number is lower than 50!")

# print(f"The number is {number}!")

# Functions

# define the function
#   'def' function_name(para1, para2,...)<---- Function header
#       block of code goes here


# def tri_area(len1, wid1):
#     areas = len1 * wid1
#     return areas


# tri_result1 = tri_area(10, 2)
# tri_result2 = tri_area(15, 2)
# tri_result3 = tri_area(1, 2)
# print(tri_result1)
# print(tri_result2)
# print(tri_result3)


# def tip(tot: float, grat: float) -> float:
#     return tot * (grat / 100)


# cost = float(input("what is the check total? "))
# gratuity = float(input("what percentage do you want to tip? "))

# tip_amount = tip(cost, gratuity)
# total = cost + tip_amount

# print(f"The tip amount should be {tip_amount} totaling {total}!")


# def has_more_characters(text1: str, text2: str) -> str:
#     result1 = len(text1)
#     result2 = len(text2)

#     if result1 > result2:
#         return f"{text1}, has more Characters!"
#     else:
#         return f"{text2}, has more Characters!"


# user_text1 = input("Please choose a word!")
# user_text2 = input("Please choose another word!")

# print(has_more_characters(user_text1, user_text2))

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# temp = int(input("What is the temperature? "))

# if temp >= 65:
#     print("Enjoy the weather!")
# elif temp >= 40:
#     print("Bring a jacket")
# else:
#     print("Wear a coat")


# num1 = int(input("Pick a starting number. "))
# num2 = int(input("Pick an ending number. "))


# def fizzbuzz(beginning, end):
#     num_list = list(range(beginning, end))
#     return num_list


# fizzbuzz(num1, num2)

# for number in num_list:
#     if number % 3 == 0 and number % 5 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("FizzBuzz")
#     else:
#         print(number)

start = int(input("Enter the Start Value: "))
stop = int(input("Enter the stop value: "))


def fizzbuzz(beginning: int, end: int) -> None:
    for number in range(beginning, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

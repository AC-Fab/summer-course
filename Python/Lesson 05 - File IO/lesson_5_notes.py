# import random

# rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """

# paper = """
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# """

# scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """

# game_image = [rock, paper, scissors]
# choice_names = ["Rock", "Paper", "Scissors"]

# while True:
#     try:
#         user_games = int(
#             input(
#                 "How many games would you like to play? Choose an odd number between 1 and 9: "
#             )
#         )
#     except ValueError:
#         print("Please enter a valid whole number.")
#         continue

#     if user_games <= 1 or user_games >= 9:
#         print("You selected too many (or too few) games. Max allowed is 9.")
#         continue
#     elif user_games % 2 == 0:
#         print("Please select an odd number.")
#         continue

#     print(f"You selected best of {user_games}!")

#     user_score = 0
#     computer_score = 0
#     games_played = 0

#     while games_played < user_games:
#         try:
#             user_choice = int(
#                 input("Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors: ")
#             )
#         except ValueError:
#             print("Invalid choice. Please try again.")
#             continue

#         if user_choice < 0 or user_choice > 2:
#             print("Invalid choice. Please try again.")
#             continue

#         computer_choice = random.randint(0, 2)
#         print("You chose:", choice_names[user_choice], game_image[user_choice])
#         print(
#             "Computer chose:",
#             choice_names[computer_choice],
#             game_image[computer_choice],
#         )

#         if user_choice == computer_choice:
#             print("It's a tie!")
#         elif (
#             (user_choice == 0 and computer_choice == 2)
#             or (user_choice == 1 and computer_choice == 0)
#             or (user_choice == 2 and computer_choice == 1)
#         ):
#             print("You win this round!")
#             user_score += 1
#         else:
#             print("You lose this round!")
#             computer_score += 1

#         games_played += 1

#     print(f"\nFinal score — You: {user_score}, Computer: {computer_score}")
#     if user_score > computer_score:
#         print("🎉 You won the match!")
#     elif user_score < computer_score:
#         print("💻 Computer won the match!")
#     else:
#         print("It's an overall tie!")

#     again = input("\nPlay again? (y/n): ").strip().lower()
#     if again != "y":
#         print("Thanks for playing!")
#         break
# import random

# with open("file.txt", "w") as f:
#     for line in range(100):
#         random_number = random.randint(50, 100)
#         f.write(str(random_number) + "\n")

# with open("file.txt", "r") as input_f:
#     lines = input_f.readlines()
#     count = 0
#     min = 1000
#     max = 0
#     sum = 0
#     for line in lines:
#         amount = int(line)
#         sum += amount
#         count += 1
#         if amount > max:
#             max = amount
#         if amount < min:
#             min = amount
#     average = sum / count

#     print(f"Max: {max}, Min: {min}, Average: {average}")

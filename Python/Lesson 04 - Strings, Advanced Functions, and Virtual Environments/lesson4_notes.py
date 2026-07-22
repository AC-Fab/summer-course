# my_list = ["c", "a", "t"]
# my_string = "cat"


# for item in my_list:
#     print(item)

# for char in my_string:
#     print(char)

# print(my_list[0], my_string[0])
# print(my_list[-1], my_string[-1])
# print(my_string[0:2])

# print(len(my_list), len(my_string))
# print("a" in my_list, "a" in my_string)

# print(list("cat"))
# user_name = input("Pick a username: ")


# def validate_username(username):
#     # Checking length of username
#     if len(username) < 5 or len(username) > 15:
#         return False
#     # Checking that username only contains letters, digits, or underscores
#     for char in username:
#         if not (char.isalpha() or char.isdigit() or char == "_"):
#             return False
#     # Checking that username starts with a letter
#     if not username[0].isalpha():
#         return False
#     # Doesn't end with underscore
#     if username[-1] == "_":
#         return False
#     # Ensure username contains at least one letter
#     has_digit = False
#     for char in username:
#         if char.isdigit():
#             has_digit = True
#             break
#     if not has_digit:
#         return False

#     return True


# validate_username(user_name)
# print(validate_username)


# Advanced function, you can give functions default parameters
# Deafualt parameters must come after required parameters
# Arguments are matched by position first, then keyword

# def curve_grades(scores, bonus=5, max_score=100):

# functions can have multiple returns

# Attempt at enumerate() function
passengers = ["Lopez", "Maria", "Alex"]


# def boarding_list(pass_list):
#     return enumerate(pass_list)


# index = list(boarding_list(passengers))
# print(index)
# print(boarding_list(passengers))

for index, passenger in enumerate(passengers, 1):
    print(index, passenger)

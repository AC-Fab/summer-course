# def greet(name):
#     message = "Hello, " + name
#     print(message)


# greet("Alice")


# def calculate_total(price, quantity):
#     total = price * quantity
#     print(f"Total: {total}")
#     return total


# calculate_total(10, 5)


# # Error 2
# def greet(name):
#     print(f"Hello, {name}")


# greet("Bob")

# # Error 1
# user_name = "Charlie"
# print(user_name)

# favorite_color = "blue"
# print(f"My favorite color is {favorite_color}")

# # Error 1
# age = 25
# message = "I am " + str(age) + " years old"
# print(message)

# # Error 2
# quantity = "5"
# price = 10.50
# total = int(quantity) * price
# print(total)

# # Error 3
# scores = [85, 90, 78, 92]
# index = "2"
# print(scores[int(index)])

# # Error 1
# fruits = ["apple", "banana", "cherry"]
# print(fruits[2])

# # Error 2
# shopping_list = ["black", "pen", "gel"]
# for item in shopping_list:
#     if item != "":
#         first_item = shopping_list[0]
#         print(first_item)
#         break
# else:
#     print("No items in your list")

# shopping_list = []
# if len(shopping_list) > 0:
#     first_item = shopping_list[0]
#     print(first_item)
# else:
#     print("Shopping list is empty")

# # Error 1
# student = {"name": "Alice", "age": 20, "major": "Computer Science", "grade": "A"}
# print(student["grade"])
# # Safer approach ####Why is this safer?####
# grade = student.get("grade", "No grade available")
# print(grade)

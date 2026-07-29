# import random

# with open("file_input.txt", "w") as f:
#     for line in range(1, 100):
#         rand_num = random.randint(50, 100)
#         f.write(str(rand_num) + "\n")

# with open("file_input.txt", "r") as input_f:
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

#     print(f"Max is : {max} Min is: {min} Average is {average}")

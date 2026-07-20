# # Getting the user inputs
# name = input("What is your name? ")
# fav_num = int(input("What is your favorite number? "))


# # create the foundation of the business card and its function
# def business_card(symbol: str, greeting: str, num_msg: int) -> none:
#     greeting = f"Hello, {name}!"
#     num_msg = f"Your favorite number is {fav_num}"
#     # determine the max length between the user inputs
#     max_len = max(len(greeting), len(num_msg))
#     # logic for dynamically creating the border
#     border_len = max_len + 4

#     border = symbol * border_len
#     # Out put the business card
#     print(border)
#     print(f"{symbol} {greeting:<{max_len}} {symbol}")
#     print(f"{symbol} {num_msg:<{max_len}} {symbol}")
#     print(border)


# business_card("|", name, fav_num)

# Need to create a range on a single line 1 to 15
# for num in range(1, 16):
#     print(num, end=" ")

# getting even numbers
# for num in range(2, 31, 2):
#     print(num, end=" ")
# countdown
# for num in range(20, -1, -2):
#     print(num, end=" ")

# # attempting to do this whole process within a function

# begin_num = int(input("Select a starting number: "))
# end_num = int(input("Select an ending number: "))
# snum = int(input("Select a step number: "))
# end_num += 1


# def print_range(start: int, stop: int, step: int) -> None:
#     for num in range(start, stop, step):
#         print(num, end=" ")


# print_range(begin_num, end_num, snum)

# # Weekly Problem set 3 - drill sergeant fitness test

# sm_name = input("What is your name? ")
# sm_rank = input("What is your rank? ")
# sm_pu = input("How many push ups do you complete? ")
# sm_2m = float(input("What was your two mile time? "))

# # Problem 4 -- Road trip fuel calculator
# # first input need the distance traveled in miles
# dist = float(input("How many miles was the trip? "))

# # Second input fuel efficiency MPG
# mpg = float(input("what is the vehicles MPG? "))

# # Third input price of gas
# cost = float(input("What is the price per gallon of gas? "))


# def rt_sum(len: float, eff: float, price: float) -> None:
#     print("---Road Trip Fuel Esitmate ---")
#     print("\n")
#     print(f"Distance:\t\t{len:.2f} miles")
#     print(f"Fuel efficiency:\t{eff:.2f} MPG")
#     print(f"Gas price:\t\t${price:.2f}/ gallon")
#     gallons = round(len / eff, 2)
#     tot_cost = round(gallons * price, 2)
#     print("\n")
#     print(f"Gallons needed:\t\t{gallons:.2f}")
#     print(f"Total Fuel Cost:\t${tot_cost:.2f}")


# print(rt_sum(dist, mpg, cost))

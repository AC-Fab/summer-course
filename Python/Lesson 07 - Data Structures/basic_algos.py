# # Basic Algorithms

# # Exercise 1

# # What is the output of this block of code?


# def mut_example(list1, list2, list3):
#     if len(list1) > 2:
#         list1 = list1[:2] #shallow copy (new list)
#     list2[0] = "hi" # modify in place
#     list3 = "".join(list2) # creates a new list


# a_list = [1, 2, 3]
# b_list = ["a", "b", "c"]
# a_str = "do-re-mi"
# mut_example(a_list, b_list, a_str)
# print(a_list)
# print(b_list) # This was the only VAr changed in the func
# print(a_str)


# # Exercise 2

# # What's the difference between sort and sorted?
# # sort cahnges the list, sorted creates a new list and is a function
# # Which one is a list method and which one is a function that works on lists?

# # Please explain


# # Exercise 3

# # Write a function that doubles the elements in a list.
# def double_list(in_list):
#     for index in range(len(int)list)):
#     in_list[index] = in_list[index] * 2


# def double_list_three(in_list):
#     new_list = []
#     for elm in in_list:
#         new_list.append(elem *2)
#     return new_list
# # Do you need to return anything here?


# # Write a function that doubles the elements in a tuple.


# # Do you need to return anything here?


# # Exercise 4

# # Rewrite the pop, count, extend, reverse, and sort functions
# def my_pop(in_list):
#     new_val = in_list[-1]
#     del in_list[-1]
#     return new_val

# def my_len(in_list):
#     len = 0
#     for elm in in_list:
#         len += 1
#     return len

# def my_count(in_list, obj):

# def my_reverse(in_list):
#     reversed = []
#     for elem in in_list[::-1]:
#         reversed.append(elem)
#     return reversed

# def my_reverse_two(in_list):
#     for index in range(len(in_list) // 2):
#         in_list[index], in_list[-index -1] = in_list[-index -1], in_list[index]


# Return the results in a new list and do not modify the original list

# (do not use the function you are rewriting)


# Exercise 5

# Fractions can be reprsented by the tuple (numerator, denominator)

# Write a function that adds two fractions


# Write a function that multiplies two fractions


# Write a function that simplifies a fraction


# Exercise 6


# write a function to calculate distance between two cartesian coordinates
# def distance(coord_one, coord_two):
#     x1, y1 = coord_one
#     x2, y2 == coord_two

# return ((x1 - x2) ** 2 + (y1 -y2)**2) **


# extension: make it work for more than two dimensions

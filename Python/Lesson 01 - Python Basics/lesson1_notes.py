#These are my lesson one notes let's see how this goes lolgit blame

pizza_size1 = int(input("What is the pizza size on the two for one deal? "))

size1_cost = float(input("How much does this deal cost? "))

pizza_size2 = int(input("What is the pizza size of one pie? "))

size2_cost = float(input("How much does this deal cost? "))

size1_area = 3.14 *(pizza_size1/2)**2

size2_area = 3.14 *(pizza_size2/2)**2

pizza1_cpa = size1_cost/(size1_area*2)

pizza2_cpa = size2_cost/size2_area

print(f"{pizza1_cpa:.2f}")

print(pizza2_cpa)
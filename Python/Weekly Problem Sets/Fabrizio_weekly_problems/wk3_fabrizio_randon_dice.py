import random

# I need to write a function  to roll a specific dice size: D6, D8, D20


def roll_dice(sides):
    return random.randint(1, sides)


# I also need to be able to roll multiple dice at the same time, starting with the same size die


def roll_many(num_dice, sides):
    rolls = []
    for x in range(num_dice):
        roll = roll_dice(sides)
        rolls.append(roll)
    return rolls


# Roll 2d6 for movement  check. Print each roll and total
num_dice = 2
sides = 6
movement_check = roll_many(num_dice, sides)
movement_sum = sum(movement_check)
print("Rolling for Movement.......")
print(
    f"Rolling {num_dice}d{sides}. Results:{movement_check}!\nFor a total movement this round of {movement_sum}!\n\n"
)
"""Alright this fixes the issue for this portion of the problem, later I want to review and try to setup the program
to have a user input the number of dice and sides need for there character. I believe I can do this with an input statement for  lines 22
and 23, instead of hard coding those numbers"""

"""Roll 1d20 for and attack check. If the result is a 20, the program should tell them it is a crictical hit.
If it is a 1 that is a crit miss. everything else is just the score."""
attack_die = 20

Roll_for_hit = roll_dice(attack_die)
print("Rolling to Attack...")
if Roll_for_hit == 20:
    print(f"{Roll_for_hit} is a Crictical Hit!\n\n")
elif Roll_for_hit == 1:
    print(f"{Roll_for_hit} is a Crictical Miss!\n\n")
else:
    print(f"you rolled a {Roll_for_hit}!\n\n")

# Roll 3d8 for damage. Print each roll, the total, and the average to 1 decimal place
num_dice = 3
sides = 8

damage_roll = roll_many(num_dice, sides)
damage_sum = sum(damage_roll)
damage_avg = damage_sum / len(damage_roll)

print("Rolling for Damage...")
print(damage_roll)
print(f"Total Damage: {damage_sum}!")
print(f"average Damage: {damage_avg:.1f}!")

"""Run the damage roll 1000 times using a for loop and track the average total damage across all runs. Print the results
How close to the Theoretical average is it. 1d8 average is 4.5"""

total = []

for trials in range(1000):
    roll = roll_dice(8)
    total.append(roll)
print(total)

average = sum(total) / len(total)

print(f"{average}")

# So now a trail assuming damage is always a 3d8 roll

trials = []

for _ in range(1000):
    roll = sum(roll_many(3, 8))
    trials.append(roll)
print(trials)

average_trial = sum(trials) / len(trials)

print(
    f"The average score of 3d8 is 13.5. This trial ran 1000 tests with and average of: {average_trial}"
)

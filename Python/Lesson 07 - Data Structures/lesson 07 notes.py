# # problem 1a
# with open("preclass_problem1_data.txt", "r") as file:
#     number = [float(line.strip()) for line in file if line.strip()]
#     print(number)

# top_5 = sorted(number, reverse=True)[:5]
# print(top_5)

# grid = sum(top_5) / 10

# print(grid)

# # Problem 1b
# with open("preclass_problem1_data.txt", "r") as file:
#     print(f"The coordinate is {sum(sorted(int(x) for x in file)[-5:])/10}")

unit = {
    "Smith": {"Rank": "Major", "years_of_service": 12},
    "Korey": {"Rank": "Specialist", "years_of_service": 4},
    "Anthony": {"Rank": "Sergeant First Class", "years_of_service": 9},
    "Holbeck": {"Rank": "Private First Class", "years_of_service": 2},
    "Patton": {"Rank": "Colonel", "years_of_service": 22},
}


def lookup_soldier(unit, last_name):
    if last_name in unit:
        info = unit[last_name]
        print(
            f"{last_name}: {info['Rank']}, {info['years_of_service']} years of service"
        )
    else:
        print(f"No soldier found with last name '{last_name}'")


lookup_soldier(unit, "Smith")


def look_upsoldier(unit, last_name):
    if last_name in unit:
        rank = unit[last_name]["Rank"]
        year_service = unit[last_name]["years_of_service"]
        print()

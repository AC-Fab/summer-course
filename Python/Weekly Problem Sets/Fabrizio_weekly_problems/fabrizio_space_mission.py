# class spacecraft:
#     def __init__(self, name, fuel_level, fuel_efficiency):
#         self.name = name
#         self.fuel_level = fuel_level
#         self.fuel_efficiency = fuel_efficiency
#         self.max_fuel = 200_000

#     def add_fuel(self, quantity):
#         self.add_fuel = min(self.max_fuel, self.fuel_level + quantity)
#         self.fuel_level = max(self.fuel_level, 0)

#     def fuel_required(self, distance):
#         amount = distance / self.fuel_efficiency
#         return amount

#     def fuel_available(self, distance):
#         return self.fuel_level >= self.fuel_required(
#             distance
#         )  # This is conceptually the same as if True else False

#     def launch(self, distance):
#         if self.fuel_available(distance):
#             self.fuel_level -= self.fuel_required(distance)
#             print(f"Launched {self.name} {distance}KM.")
#         else:
#             print(f"{self.name} does't have enough fuel to travel {distance}!")


# sp1 = spacecraft("Vostok 1", 250, 1.5)
# sp2 = spacecraft("Voyager 1", 400, 2.0)

# sp1.launch(500)
# sp2.launch(350)


class planet:
    def __init__(self, name, coords, danger, resources, atmosphere):
        self.name = name
        self.coords = coords
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere

    def __str__(self) -> str:
        return f"Planet {self.name} is located at {self.coords} which is danger {self.danger} rated.\n\nThough it does have {self.resources} resources, the atmosphere is {self.atmosphere} plan accordingly!\n"

    def __sub__(self, other):
        x1, y1, z1 = self.coords
        x2, y2, z2 = other.coords
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5


earth = planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like")
mars = planet("Mars", (227.9, 0.0, 1.0), 1, 20, "Thin")
jupiter = planet("Jupiter", (778.5, 50.0, 12.0), 3, 40, "Gas Giant")
saturn = planet("Saturn", (1434.0, -80.0, -20.0), 2, 35, "Gas Giant")
uranus = planet("Uranus", (2871.0, 30.0, 40.0), 2, 45, "Icy")

print(earth)
print(mars)
print(saturn)
print(earth.__sub__(mars))

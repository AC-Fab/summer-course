"""Import the math module.
Write a function distance(x1, y1, x2, y2) that calculates the straight-line distance between
two points in space using the distance formula. Use math.sqrt().

Write a function orbit_circumference(radius) that calculates the circumference of a circular orbit. Use math.pi.

Write a function fuel_needed(mass, velocity) that calculates kinetic energy as 0.5 * mass * velocity ** 2,
then returns the result rounded to 2 decimal places using math.floor().

Use the functions to print a navigation report for the following mission data:
ship_pos    = (0, 0)
station_pos = (143, 892)
orbit_radius = 6371        # km (Earth's radius)
ship_mass    = 50000       # kg
ship_velocity = 7800       # m/s
Also print math.log(ship_velocity, 10) and explain in a comment what this value represents.
Expected output:

=== NAVIGATION REPORT ===
Distance to station:    902.35 units
Orbit circumference:    40030.17 km
Kinetic energy (fuel):  1520100000000.0 J
Log10 of velocity:      3.89
"""

import math

# Write a function distance(x1, y1, x2, y2) that calculates the straight-line distance between
# two points in space using the distance formula. Use math.sqrt()


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt((dx**2) + (dy**2))
    return distance


# print(distance(0, 0, 3, 4)) # Sanity check the ouput should be 5.0 for a classic right triangle

# Write a function orbit_circumference(radius) that calculates the circumference of a circular orbit. Use math.pi.


def orbit_circumference(radius):
    edge_len = 2 * math.pi * radius
    return edge_len


# print(orbit_circumference(2)) #This was a sanity check I validated with [1, 0.5, 2] then checked linearity of outcome

# Write a function fuel_needed(mass, velocity) that calculates kinetic energy as 0.5 * mass * velocity ** 2,
# then returns the result rounded to 2 decimal places using math.floor().


def fuel_needed(mass, velocity):
    kin_energy = 0.5 * mass * velocity**2
    print(kin_energy)
    result = math.floor(kin_energy * 100) / 100
    return result


print(fuel_needed(3, 7.356))

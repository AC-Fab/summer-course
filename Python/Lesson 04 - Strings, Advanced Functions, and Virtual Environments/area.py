# creating functions a my own module
# rectangle area
def rectangle_area(leng: float, widt: float) -> float:
    return leng * widt


# circle area
def circle_area(radius: int) -> int:
    return 3.1415 * radius**2


# triangle area
def tri_area(base: float, height: float) -> float:
    return 0.5 * base * height

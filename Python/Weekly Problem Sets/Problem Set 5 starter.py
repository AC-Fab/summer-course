# recursive_squares(n) I need a base case, the recursion call and something to return

"""recursive_squares(5)
[1, 4, 9, 16, 25]"""


def recursive_squares(n: int) -> list:  # ? I think this is correct
    if n == 0:
        return []
    smaller = recursive_squares(n - 1) + [n**2]

    return smaller

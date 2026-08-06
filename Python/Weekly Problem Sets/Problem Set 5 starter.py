# recursive_squares(n) I need a base case, the recursion call and something to return

"""recursive_squares(5)
[1, 4, 9, 16, 25]"""


def recursive_squares(n: int) -> list:  # ? I think this is correct
    if n == 0:
        return []
    smaller = recursive_squares(n - 1) + [n**2]

    return smaller


# palindrome checker first stepp everything should be lowercase after input, to account for the case insensitive
def palindrome_checker(text: str) -> bool:
    text = text.lower()
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome_checker(text[1:-1])

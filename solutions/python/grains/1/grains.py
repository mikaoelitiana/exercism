CHESSBOARD_SQUARES = 64


def square(number):
    if number > CHESSBOARD_SQUARES or number < 1:
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return 1
    return 2 * square(number - 1)


def total():
    total = 0
    for i in range(0, CHESSBOARD_SQUARES):
        total += square(i + 1)
    return total

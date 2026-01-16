def is_armstrong_number(number):
    digits = list(str(number))
    length = len(digits)
    sum_of_powers = 0
    for digit in digits:
        sum_of_powers += pow(int(digit), length)
    return number == sum_of_powers

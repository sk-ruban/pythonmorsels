roman_dict = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def int_to_roman(number):
    result = ""
    for (hindu, roman) in roman_dict:
        # takes two numbers and returns a pair of numbers (a tuple) of quotient and remainder
        (factor, number) = divmod(number, hindu)
        result += roman * factor
    return result


def roman_to_int(number):
    result = ""


int_to_roman(5)
int_to_roman(8)
int_to_roman(14)
roman_to_int('IIII')
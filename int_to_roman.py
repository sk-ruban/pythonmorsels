convert_table = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}


def int_to_roman(num):
    roman = []
    # .items() to return the k,v of a dict
    for k, v in convert_table.items():
        # // floor division - return w/o remainder
        roman.append(num//k * v)
        # % returns the remainder
        num %= k
    # "".join() - joins elements of an iterable together
    return "".join(roman)


def roman_to_int(num):
    ix = 0
    result = 0
    while ix < len(num):
        for k, v in convert_table.items():
            if num.startswith(v, ix):
                result += k
                ix += len(v)
                break
        else:
            raise ValueError('Invalid Roman number.')
    return result


# Base + Bonus 1
int_to_roman(5)
int_to_roman(4)
int_to_roman(9)

# Bonus 2
roman_to_int('I')
roman_to_int('MDCCLXXXVI')
roman_to_int("XVA")

# Bonus 3
roman_to_int('IV')
roman_to_int('MCMXLVIII')
#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or not roman_string:
        return (0)
    roman_nums = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50),
                       ('C', 100), ('D', 500), ('M', 1000)])
    number_int = 0
    for rom_num1, rom_num2 in zip(roman_string, roman_string[1:]):
        if roman_nums[rom_num1] < roman_nums[rom_num2]:
            number_int -= roman_nums[rom_num1]
        else:
            number_int += roman_nums[rom_num1]
    number_int += roman_nums[roman_string[-1]]
    return number_int

"""
title: function_lab
author: Akshin Vemana
date: 6/26/2019 3:32 PM
"""
import math


def age_calculator(year1, year2):
    return abs(year1 - year2)


def avg_three_numbers(num1, num2, num3):
    return (num1 + num2 + num3) / 3


def avg_numbers(*args):
    return (math.fsum(args)) / (len(args))


print(age_calculator(2018, 1900))
print(avg_three_numbers(4, 7, 8))
print(avg_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9))

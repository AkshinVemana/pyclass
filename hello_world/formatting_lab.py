"""
title: formatting_lab
author: Akshin Vemana
date: 6/26/2019 10:10 AM
"""

import random

name = input("What's your name?")
salary = int(input(f"Hi, {name}! How much do you make?"))
raise_per = random.randint(0, 100)
raise_amount = salary * raise_per / 100
new_salary = salary + raise_amount
print(f"{name}, your new salary is {new_salary}")
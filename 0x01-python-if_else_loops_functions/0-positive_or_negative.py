#!/usr/bin/python3
from random import randrange
number = randrange(-10, 11)
if number == 0:
	print(f"{number} is zero")
elif number > 0:
	print(f"{number} is positive")
else:
	print(f"{number} is negative")

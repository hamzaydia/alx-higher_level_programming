#!/usr/bin/python3
numbers = []
for i in range(0, 10):
    for j in range(i + 1, 10):
        numbers.append("{}{}".format(i, j))
output = ", ".join(numbers)
print(output)

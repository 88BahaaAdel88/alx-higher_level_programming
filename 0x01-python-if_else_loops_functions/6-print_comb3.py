#!/usr/bin/python3

for i in range(9):
    for j in range(10):
        if j == i:
            continue
        result = f"{i}{j}"
        print("{:s}".format(result), end='\n' if result == '89' else ', ')

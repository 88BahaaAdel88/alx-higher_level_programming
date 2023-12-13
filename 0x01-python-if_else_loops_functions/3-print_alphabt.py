#!/usr/bin/python3

ascii_code = 97

for i in range(26):
    if i == 4 or i == 16:
        ascii_code += 1
        continue
    print('{}'.format(chr(ascii_code)), end='')
    ascii_code += 1

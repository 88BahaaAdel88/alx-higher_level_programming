#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):  # Range should start from 1, not 0
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end=" ")
        elif i % 3 == 0:
            print('Fizz', end=" ")
        elif i % 5 == 0:
            print('Buzz', end=" ")
        else:
            print(i, end=" ")

#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the 'fizzBuzz' function below.
# The function accepts INTEGER n as parameter.


def fizzBuzz(n):
    i = 0
    while (i < n):
        # m = int(input().strip())
        i = i + 1
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

    # Write your code here


if __name__ == '__main__':
    # x=0
    # while(x<n):
    n = int(input().strip())
    # if (n/3)==int and (n/5)==int:
    #         print("FizzBuzz")
    # elif (n/3)==int:
    #     print("Fizz")
    # elif (n/5)==int:
    #     print("Buzz")
    # else:
    #     print(n)

    fizzBuzz(n)
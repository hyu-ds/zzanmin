import sys
input = sys.stdin.readline

import math

def R(x):
    if x%1 >= .5:
        return math.ceil(x)
    elif x%1 < .5:
        return math.floor(x)

n = int(input())

if n != 0:
    numbers = []

    for i in range(n):
        numbers.append(int(input()))

    numbers.sort()

    m = R(n*0.15)

    print(R(sum(numbers[m:n-m])/(n-2*m)))

else:
    print(0)
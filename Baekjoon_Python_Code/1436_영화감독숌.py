import sys
input = sys.stdin.readline

N = int(input())

numbers = []
number = 666
cnt = 1

while cnt <= N:
    if '666' in str(number):
        numbers.append(number)
        cnt += 1
    number += 1

print(numbers[-1])
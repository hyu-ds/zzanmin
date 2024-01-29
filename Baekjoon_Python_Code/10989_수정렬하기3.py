import sys
input = sys.stdin.readline

## 메모리 제한과 시간제한이 중요한 문제

N = int(input())

numbers = [0 for i in range(10001)]

for i in range(N):
    number = int(input())
    numbers[number] += 1

for i in range(10001):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)
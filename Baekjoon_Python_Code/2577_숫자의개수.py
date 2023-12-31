import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

N = A*B*C

lst = [0 for i in range(10)]
nlst = list(str(N))

for i in nlst:
    lst[int(i)] += 1

for i in lst:
    print(i)
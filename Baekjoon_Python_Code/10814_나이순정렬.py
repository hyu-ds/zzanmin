import sys
input = sys.stdin.readline

N = int(input())

info = []

for idx, i in enumerate(range(N)):
    age, name = input().strip('\n').split()
    info.append([idx+1, int(age), name])

info.sort(key=lambda x: (x[1], x[0]))

for k in info:
    print(k[1], k[2])
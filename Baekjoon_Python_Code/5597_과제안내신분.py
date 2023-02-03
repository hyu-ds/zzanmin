import sys
input = sys.stdin.readline
num = []
for i in range(28):
    n = int(input())
    num.append(n)
for i in range(1, 31):
    if i in num:
        pass
    else:
        print(i)
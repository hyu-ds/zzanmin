import sys
input = sys.stdin.readline

N = int(input())

dots = [4]

for i in range(N):
    dot = dots[i]**(1/2) + dots[i]**(1/2)-1
    dots.append(int(dot**2))
print(dots[N])
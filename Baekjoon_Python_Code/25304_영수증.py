import sys
input = sys.stdin.readline

X = int(input())
N = int(input())
Sum = 0
for i in range(N):
    a, b = input().rstrip().split()
    Sum += int(a) * int(b)
if Sum == X:
    print("Yes")
else:
    print("No")
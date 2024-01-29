import sys
input = sys.stdin.readline

T = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]

for n in range(3, 41):
    zero.append(zero[n-1]+zero[n-2])
    one.append(one[n-1]+one[n-2])

for i in range(T):
    N = int(input())
    print(zero[N], one[N])
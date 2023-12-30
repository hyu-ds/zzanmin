import sys
input = sys.stdin.readline

def reverse(x):
    x = (x%10)*100 + ((x//10)%10)*10 + x//100
    return x

n1, n2 = map(int, input().strip('/n').split())

r_n1 = reverse(n1)
r_n2 = reverse(n2)

if r_n1 > r_n2:
    print(r_n1)
else:
    print(r_n2)
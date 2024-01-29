import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    nlst = list(str(n))
    if nlst == nlst[::-1]:
        print('yes')
    else:
        print('no')
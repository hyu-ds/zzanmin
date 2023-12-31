import sys
input = sys.stdin.readline

def isRectangle(a, b, c):
    if a**2 == b**2 + c**2:
        print('right')
    else:
        print('wrong')

while True:
    a, b, c = list(map(int, input().split()))

    if a+b+c == 0:
        break

    if a > b and a > c:
        isRectangle(a, b, c)

    elif b > c and b > a:
        isRectangle(b, c, a)

    elif c > a and c > b:
        isRectangle(c, a, b)

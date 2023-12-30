import sys
input = sys.stdin.readline

"""
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    elif a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
"""
_w = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]

def w(a, b, c):
    global _w
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        if _w[20][20][20] != 0:
            return _w[20][20][20]
        _w[20][20][20] = w(20, 20, 20)
        return _w[20][20][20]

    elif a < b and b < c:
        if _w[a][b][c] != 0:
            return _w[a][b][c]
        _w[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return _w[a][b][c]

    else:
        if _w[a][b][c] != 0:
            return _w[a][b][c]
        _w[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return _w[a][b][c]

a, b, c = 0, 0, 0

while True:
    a, b, c = map(int, input().strip('\n').split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')

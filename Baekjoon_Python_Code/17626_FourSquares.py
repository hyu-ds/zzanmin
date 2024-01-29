import sys
input = sys.stdin.readline

# 1<=n<=50000

n = int(input())

squares = [i*i for i in range(1, 224)]

squaresum = []

for i in squares:
    for j in squares:
        squaresum.append(i+j)

squaresum.sort()

def fourSquares(i, squares, squaresum):
    if i in squares:
        return 1
    elif i in squaresum:
        return 2
    else:
        j =0
        while squaresum[j] < i:
            if i - squaresum[j] in squares:
                return 3
            j += 1
    return 4

print(fourSquares(n, squares, squaresum))
import sys
input = sys.stdin.readline

tile = [0, 1, 3]

n = int(input())

for i in range(3, 1001):
    if i%2!=0:
        tile.append(2*tile[i-1]-1)
    else:
        tile.append(2*tile[i-1]+1)

print(tile[n]%10007)
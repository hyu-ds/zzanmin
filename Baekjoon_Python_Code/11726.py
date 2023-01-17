import sys

n = int(sys.stdin.readline())
arr = [0] * 1001

for i in range(1001):
    if i == 0:
        arr[i] = 0
    elif i == 1:
        arr[i] = 1
    elif i == 2:
        arr[i] = 2
    else:
        arr[i] = arr[i-1] + arr[i-2]
print(arr[n]%10007)
 
N = int(input())
Sum = 1
i = 0

while True:
    Sum += 6*i
    if N <= Sum:
        print(i+1)
        break
    else:
        i += 1
import sys

def Sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] >= arr[j]:
                (arr[i], arr[j]) = (arr[j], arr[i])
            else:
                pass
    return arr

def Aver(arr, N):
    sum = 0
    for i in range(N):
        sum += arr[i]
    aver = sum/N
    print(round(aver))

def Med(arr, N):
    print(arr[int((N+1)/2)-1])

def mode(arr, N):
    number = []
    for i in range(N):
        maxi = 1
        for j in range(i+1, N):
            if arr[i] == arr[j]:
                maxi += 1
            else:
                number.append((arr[i], maxi))
                break
    number.sort(key = lambda x : x[0])
    count = 0
    for i in range(len(number)):
        if number[i][1] == number[-1][1]:
            count += 1
            if count == 2:
                print(number[i][0])
                break
            else:
                pass
        else:
            pass
    if count != 2:
        print(number[-1][1])
        

def Range(arr, N):
    print(arr[N-1]-arr[0])

N = int(sys.stdin.readline().strip('\n'))
arr = [0] * N
for i in range(N):
    arr[i] = int(sys.stdin.readline().strip('\n'))
arr = Sort(arr)
Aver(arr, N)
Med(arr, N)
mode(arr, N)
Range(arr, N)


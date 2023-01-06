def ARR(A, B, arr):
    for i in range(A, A+10):
        for j in range(B, B+10):
            if arr[i][j] == True:
                arr[i][j] = True
            else:
                arr[i][j] = False
    return arr

arr = [[True for col in range(100)] for row in range(100)]

arr = ARR(0, 0, arr)

print(arr)


def Sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] >= arr[j]:
                (arr[i], arr[j]) = (arr[j], arr[i])
            else:
                break
    print(arr)

arr = [1, 5, 4, 3, 2]
Sort(arr)


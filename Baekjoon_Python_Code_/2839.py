N = int(input())
_5kg = 0
_3kg = 0


if N % 5 == 0:
    print(N // 5)
else:
    result = -1
    for i in range((N//5)+1):
        if (N - 5 * i) % 3 == 0:
            result = i + ((N - 5 * i) // 3)
    print(result)



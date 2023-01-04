number = int(input())
Sum = 0
i = 1

while True:
    Sum += i
    if number <= Sum:
        if (i % 2) == 0:
            print("%s/%s" %(((i-(Sum - number)), (1+(Sum - number)))))
        else:
            print("%s/%s" %((1+(Sum - number)), (i-(Sum - number))))
        break
    else:
        i += 1
        continue
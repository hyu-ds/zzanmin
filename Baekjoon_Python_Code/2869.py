A, B, V = map(int, input().split(" "))

while True:
    if (V - A) % (A - B) == 0:
        print(int((V - A) / (A - B)) + 1)
        break
    else:
        if (V - A) < (A - B):
            print(2)
        else:
            print(int((V - A) / (A - B)) + 2)
        break
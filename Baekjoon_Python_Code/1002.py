import math

T = int(input())
i =0

while i < T:
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    ABS = abs(r1-r2)

    if (ABS == distance != 0) or ((r1 + r2) == distance):
        print(1)
    elif (ABS > distance) or ((r1 + r2) < distance):
        print(0)
    elif (r1 == r2) and (distance == 0):
        print(-1)
    else:
        print(2)
    i += 1





    



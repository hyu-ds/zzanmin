from functools import cache

@cache
def People_Num(floor, room):
    number = 0
    if floor == 0:
        number = room
    else:
        for i in range(room):
            number += People_Num(floor-1, i+1)
    return number

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(People_Num(k, n))
T = int(input())

for i in range(T):
    H, W, N = map(int, input().split(" "))
    room = (N//H)+1
    floor = (N%H)
    if floor == 0:
        room -= 1
        floor = H
    print(f'{floor*100 + room}')
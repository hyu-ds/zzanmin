import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

blocks = []

for i in range(N):
    blocks.append(list(map(int, input().split())))

min_time = 256*500*500 + 2*256*500*500
max_target = 0

for target in range(257):
    time = 0
    needed = 0
    block = B
    for n in range(N):
        for m in range(M):
            if blocks[n][m] > target:
                time += 2*(blocks[n][m]-target)
                block += blocks[n][m]-target
            elif blocks[n][m] < target:
                time += target-blocks[n][m]
                needed += target-blocks[n][m]
    if needed <= block:
        if min_time > time:
            min_time = time
            max_target = target

print(min_time, max_target)
    
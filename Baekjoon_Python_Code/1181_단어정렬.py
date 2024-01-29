import sys
input = sys.stdin.readline

N = int(input())

words = []

for i in range(N):
    word = input().strip('\n')
    if word not in words:
        words.append(word)

words.sort()
cnt = 0

for i in range(1, 51):
    for w in words:
        if len(w) == i:
            print(w)
            cnt += 1
    if cnt > N:
        break
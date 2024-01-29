import sys
input = sys.stdin.readline

N, M = map(int, input().split())

note = {}

for i in range(N):
    site, pw = input().strip('\n').split()
    note[site] = pw

for i in range(M):
    site = input().strip('\n')
    print(note[site])
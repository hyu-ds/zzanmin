import sys
input = sys.stdin.readline

s = input()

alphabet = {}

for n in range(ord("a"), ord("z")+1):
    alphabet[chr(n)] = -1

for i in range(len(s)-1):
    if alphabet[s[i]] == -1:
        alphabet[s[i]] = i

for j in range(ord("a"), ord("z")+1):
    print(alphabet[chr(j)], end=' ')


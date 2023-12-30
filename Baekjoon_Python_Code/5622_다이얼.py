import sys
input = sys.stdin.readline

Alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

s = list(input().strip('\n'))
n = 0

for i in s:
    for j in Alphabet:
        if i in j:
            n += Alphabet.index(j) + 3

print(n)
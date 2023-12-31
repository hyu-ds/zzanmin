import sys
input = sys.stdin.readline

def measure(n:int):
    measures = []
    for i in range(1, n):
        if n%i == 0:
            measures.append(i)
    return measures

while True:
    n = int(input())
    if n == -1:
        break
    m = measure(n)
    if sum(m) == n:
        print(f'{n} = ', end='')
        print(*m, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')
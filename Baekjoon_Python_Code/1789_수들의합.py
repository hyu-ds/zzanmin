import sys
input = sys.stdin.readline

S = int(input())

def N_max(S):
    n = 1
    s = 0
    while S >= s:
        s += n
        n += 1
    return n-2

## 서로 다른 n개의 수를 더하고 남을 수 있는 가장 큰 수는 n-1이다.
## n-1 중 n에 k를 더하면, n부터 n+k-1까지 더하지 않은 수가 생기지만, 아무리 수가 커도 n-1-k이기 때문에 수를 더 늘릴 수 없다.
## 따라서 서로 다른 n개의 수를 1씩 더해서 S를 넘지 않는 N이 답이다.

print(N_max(S))
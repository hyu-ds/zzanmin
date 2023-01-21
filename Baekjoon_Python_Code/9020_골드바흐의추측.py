import sys

def checkprime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True


T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    a = n//2
    b = n//2
    while a>0:
        if checkprime(a) and checkprime(b):
            print('%d %d'%(a, b))
            break
        else:
            a -= 1
            b += 1

## 짝수의 절반에서 +1 -1을 해가면서 더하고 뺀 수들이 소수인지 확인하는 코드를 작성한다.
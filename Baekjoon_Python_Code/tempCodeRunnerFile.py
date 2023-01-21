import sys

def isprime(n, arr):  
    primes = []
    for i in range(2, (2*n)+1):
        if arr[i]:
            for j in range(2*i, (2*n)+1, i):
                arr[j] = False
            if i > n:
                primes.append(i)
    print(len(primes))

arr = [False]*2 + [True]*(2*123456-1)
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    isprime(n, arr)
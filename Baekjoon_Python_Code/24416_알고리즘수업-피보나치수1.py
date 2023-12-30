# 동적 프로그램(Dynamic Programming)은 '재활용 프로그래밍'으로 생각할 수 있다.
# 즉, 이전에 사용한 계산결과를 다시 사용하는 것과 다름이 없다.

import sys
input = sys.stdin.readline

count_r = 0
count_d = 0

def recursion_fibo(n):  #재귀 프로그램
    global count_r
    if n == 1 or n == 2:
        count_r += 1
        return 1    # 코드 1
    else:
        return (recursion_fibo(n - 1) + recursion_fibo(n - 2))

def dynamic_fibo(n):   #동적 프로그래밍
    global count_d
    
    f = [1 for i in range(n+1)]
    for i in range(3, n+1):
        f[i] = f[i - 1] + f[i - 2]  # 코드 2
        count_d += 1
    return f[n]

n = int(input())
count_r = dynamic_fibo(n)

print(f'{count_r} {count_d}')

# 🔥 이창민의 백준 뿌셔 🔥

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=dlckdals0204)](https://solved.ac/dlckdals0204/)
<br>

## 시작한 날 : 2022년 12월 30일
## 목표 : **실버 V**
### <br>풀이 일기
---
날짜 : 2022.12.30.  
푼 문제 : test
``` Python
print("Hello, World!")
```
print로 출력만 하면 된다.

---
날짜 : 2023.01.01.  
푼 문제 : No.1712 - 손익분기점
``` Python
A, B, C = map(int, input().split(' '))

if C!=B:
    Break_Even_Point = A/(C-B)

    if Break_Even_Point > 0:
        print(int(Break_Even_Point)+1)
    else:
        print(-1)
else:
    print(-1)
```
가격과 가변비용이 같을 때와 다를 때를 구분한다.(ZeroDivision 주의)

두 값이 다를 때, 양수일 때와 음수일 때를 구분한다.

---
푼 문제 : No.2292 - 벌집
``` Python
N = int(input())
Sum = 1
i = 0

while True:
    Sum += 6*i
    if N <= Sum:
        print(i+1)
        break
    else:
        i += 1
```
숫자가 일정하게 증가한다는 것을 이용하자.

---
푼 문제 : No.1193 - 분수찾기
``` Python
number = int(input())
Sum = 0
i = 1

while True:
    Sum += i
    if number <= Sum:
        if (i % 2) == 0:
            print("%s/%s" %(((i-(Sum - number)), (1+(Sum - number)))))
        else:
            print("%s/%s" %((1+(Sum - number)), (i-(Sum - number))))
        break
    else:
        i += 1
        continue
```
짝수번째와 홀수번째 분수가 변하는 양상이 다름을 이용하자.

---
푼 문제 : No.2869 - 달팽이는 올라가고 싶다
``` Python
A, B, V = map(int, input().split(" "))

while True:
    if (V - A) % (A - B) == 0:
        print(int((V - A) / (A - B)) + 1)
        break
    else:
        if (V - A) < (A - B):
            print(2)
        else:
            print(int((V - A) / (A - B)) + 2)
        break
```
일반적으로 A를 더해가면서 날짜를 세면 시간초과가 걸린다.

더하기는 곧 곱하기이고, 이는 나누기와 관련이 있음을 생각하자.

---
푼 문제 : No.10250 - ACM 호텔
``` Python
T = int(input())

for i in range(T):
    H, W, N = map(int, input().split(" "))
    room = (N//H)+1
    floor = (N%H)
    if floor == 0:
        room -= 1
        floor = H
    print(f'{floor*100 + room}')
```
H가 N으로 나누어떨어지는, 즉 floor가 0이 되는 부분에 주의하자.

---
푼 문제 : No.2775 - 부녀회장이 될테야
``` Python
from functools import cache

@cache
def People_Num(floor, room):
    number = 0
    if floor == 0:
        number = room
    else:
        for i in range(room):
            number += People_Num(floor-1, i+1)
    return number

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(People_Num(k, n))
```
재귀함수를 사용할 때, 변수를 헷갈리지 말고 잘 넣어주자.

맨 위의 조건 없이는 시간초과가 걸린다.(파이썬의 한계?)

---
푼 문제 : No.2839 - 설탕 배달
``` Python
N = int(input())

if N % 5 == 0:
    print(N // 5)
else:
    result = -1
    for i in range((N//5)+1):
        if (N - 5 * i) % 3 == 0:
            result = i + ((N - 5 * i) // 3)
    print(result)
```
나머지와 몫, 그리고 뺄셈을 잘 활용해야하는 문제였다.

케이스를 잘 따져보자.

---
푼 문제 : No.10757 - 큰 수 A+B
``` Python
A, B = map(int, input().split(" "))

print(A+B)
```
파이썬은 자연수의 크기에 구애받지 않고 다룰 수 있지만, C와 C++은 자료형마다 저장할 수 있는 크기가 정해져 있다는 것을 생각해볼 수 있는 문제다.

---
날짜 : 2023.01.02.  
푼 문제 : test
``` Python
print("Hello, World!")
```
print로 출력만 하면 된다
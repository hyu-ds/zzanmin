# 🔥 이창민의 백준 뿌셔 🔥


[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=dlckdals0204)](https://solved.ac/dlckdals0204/)
<br>

## 시작한 날 : 2022년 12월 30일
## 목표 : **실버 V**
### 🌟 sys.stdin.readline() 🌟
보통 파이썬을 사용할 때 입력을 아래와 같이 받는다.
```python
A_Number = int(input())
Numbers = map(int, input().split())
List_of_Numbers = list(map(int, input().split()))
```
하지만 위와 같은 방법은 **시간초과**를 만날 가능성이 있다.
따라서 앞으로는 입력을 받을 때, 아래와 같은 방법을 사용할 것이다.
```python
import sys #sys라는 툴을 받아준다.
A_Number = int(sys.stdin.readline())
Numbers = map(int, sys.stdin.readline().strip('\n').split())
List_of_Numbers = list(map(int, sys.stdin.readline().strip('\n').split()))
```
여기서 중요한 점은 **int**형태로 받아주어야한다는 점이다.
sys.stdin.readline()은 str형태로 입력받는다는 특징이 있는데,
개수를 입력받아 for문을 돌리거나 사칙연산을 하는 것과 같은 동작을 수행하기 위해서는 정수형으로 바꾸어 주어야 할 필요성이 있다. 꼭 'int'로 받는 것을 잊지말자 ! ! !
### 🌟 에라토스테네스의 체 🌟
소수는 자기 자신과 1 외에 나누어지는 수가 없는 수를 뜻한다. 따라서 소수를 구하기 위해서는 다른 수로 나누어지는지 확인해 보면 된다. 아래의 코드를 보자.
```python
N = 100
primes = []
for i in range(2, N):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            isprime = False
    if isprime:
        primes.append(i)
```
이 코드는 특정 수가 소수인지 판별하여 리스트에 추가하는 코드이다. 이를 판별하기위해 코드에서는 특정 수보다 작은 모든 수로 나누어 보고 나누어지는 수가 없으면 리스트에 추가한다. 이는 시간이 많이 걸린다는 단점이 있다.<br>
이를 해결하기 위해 고안된 방식이 **에라토스테네스의 체**이다. 에라토스테네스의 체에서는 소수의 배수를 모두 찾아내어 그 수들을 소수에서 배제한다. 따라서 수가 커질 수록 배제된 수들이 늘어나 확인해야할 수도 같이 줄어들며, 이와 동시에 시간도 절약된다. 이를 표현한 코드는 아래와 같다.
```python
N = 100
arr = [False] * 2 + [True] * [N-1] # 0과 1은 소수가 아니므로 미리 False로 저장해준다.
primes = []
for i in range(2, N+1):
    if arr[i]: #True라면 lsit에 추가한다.
        primes.append(i)
    for j in range(2*i, N+1, i): #i의 2배수부터 i를 더해가면서 소수 i의 배수를 배제해나간다.
        arr[j] = False
```
위의 방식을 사용하면 소수를 찾는 문제에서 시간초과가 생기는 문제를 해결할 수 있다. 두 코드의 공통점은 모두 True와 False를 사용한다는 점을 잊지말고 잘 활용해보자.
### <br>🖥️ 풀이 일기 🖥️
---
날짜 : 2022.12.30.  
푼 문제 : test
``` Python
print("Hello, World!")
```
2022.12.30 백준 스터디 기동실행
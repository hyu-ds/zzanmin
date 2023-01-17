# 🔥 이창민의 백준 뿌셔 🔥


[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=dlckdals0204)](https://solved.ac/dlckdals0204/)
<br>

## 시작한 날 : 2022년 12월 30일
## 목표 : **실버 V**
### 🌟 sys.stdin.readline() 🌟
보통 파이썬을 사용할 때 입력을 아래와 같이 받는다
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
수의 개수를 입력받아 for문을 돌리거나 사칙연산을 하는 것과 같은 동작을 수행하기 위해서는 문자형을 바꾸어 주어야 할 필요성이 있다. 꼭 'int'로 받는 것을 잊지말자 ! ! !
### <br>풀이 일기
---
날짜 : 2022.12.30.  
푼 문제 : test
``` Python
print("Hello, World!")
```
2022.12.30 백준 스터디 기동실행
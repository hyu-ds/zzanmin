import sys
input = sys.stdin.readline

N = int(input())

numbers = [int(input()) for i in range(N)]

numbers.sort()

if sum(numbers)/N > 0:
    print(int(sum(numbers)/N+.5))
else:
    print(int(sum(numbers)/N-.5))

print(numbers[int(N/2)])
    
# round 함수를 사용할 때는 4사 5입을 주의하자

cnt = {}

for i in numbers:
    cnt[i] = 0

for i in numbers:
    cnt[i] += 1

mode = 0

for i in numbers:
    if mode < cnt[i]:
        mode = cnt[i]

number = []

for i in set(numbers):
    if cnt[i] == mode:
        number.append(i)

number.sort()

if len(number) > 1:
    print(number[1])
else:
    print(number[0])

print(max(numbers) - min(numbers))
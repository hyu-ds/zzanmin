import sys

n = int(sys.stdin.readline())
stack = []
answer = []
count = 1
flag = 0
for i in range(n):
    number = int(sys.stdin.readline())
    while count <= number:
        answer.append("+")
        stack.append(count)
        count += 1
    if stack[-1] == number:
        answer.append("-")
        stack.pop()
    else:
        flag = 1
        print("NO")
        break
if flag == 0:
    for i in answer:
        print(i)
            
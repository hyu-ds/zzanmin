### "[", "]", "(", ")" 하나만 있는 경우를 고려해주어야 한다.
### 문자열 자체를 스택으로 이용하기 보다는 스택을 하나 만들어 주어 활용하는 방향으로 문제를 풀어야 한다. 

import sys

def check(Words):
    stack = []
    isVPS = True
    for i in range(len(Words)):
        if Words[i] == "[" or Words[i] == "(":
            stack.append(Words[i])
        elif Words[i] == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break
        elif Words[i] == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
        else:
            pass
    if len(stack) != 0:
        isVPS = False
    return isVPS


while True:
    Words = []
    Words = list(sys.stdin.readline().strip("\n"))
    if Words[0] == ".":
        break
    if check(Words):
        print("yes")
    else:
        print("no")


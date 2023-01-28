import sys

def isVPS(stack):
    count = 0
    isvps = True
    if len(stack)%2 != 0:
        isvps = False
    else:
        for i in range(len(stack)):
            if stack[-1] == ")":
                count += 1
            else:
                count -= 1
            stack.pop()
            if count < 0:
                isvps = False
                break
        if count != 0:
            isvps = False
    return isvps

T = int(sys.stdin.readline())
stack = []
for i in range(T):
    stack = list(sys.stdin.readline().strip('\n'))
    if isVPS(stack):
        print("YES")
    else:
        print("NO")
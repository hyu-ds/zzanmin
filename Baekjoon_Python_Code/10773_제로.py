import sys

def push(stack, n):
    stack.append(n)
    return stack
def pop(stack):
    stack.pop()
    return stack

K = int(sys.stdin.readline())
stack = []
for i in range(K):
    n = int(sys.stdin.readline().strip("\n"))
    if n != 0:
        push(stack, n)
    else:
        pop(stack)
print(sum(stack))
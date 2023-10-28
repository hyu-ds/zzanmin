import sys
input = sys.stdin.readline

A = int(input())
S = input().strip("\n")
B = int(input())

if S == "+":
    print(A+B)
if S == "*":
    print(A*B)
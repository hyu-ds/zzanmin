import sys
input = sys.stdin.readline

def isPalindrome(s:str) -> int:
    s_copy = s[::-1]
    if s == s_copy:
        return 1
    else:
        return 0
    
s = input().strip('\n')

print(isPalindrome(s))
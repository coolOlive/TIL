import sys
input=sys.stdin.readline

# 스택/괄호의 값/실버1

s=input().strip()
n = len(s)
tmp = 1
answer = 0
stack = []

for i in range(n):
    if s[i] == '(':
        stack.append(s[i])
        tmp *= 2
    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            answer=0
            break
        elif s[i-1] == '(':
            answer += tmp
        tmp //= 2
        stack.pop()
            
    elif s[i] == '[':
        tmp *= 3
        stack.append(s[i])
    else:
        if not stack or stack[-1] == '(':
            answer=0
            break
        elif s[i-1] == '[':
            answer += tmp
        tmp //= 3
        stack.pop()

if stack:
    answer=0
print(answer)
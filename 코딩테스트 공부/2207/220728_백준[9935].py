import sys
input=sys.stdin.readline

# 문자열,스택_문자열 폭발/골드4

s=input().strip()
bomb=input().strip()
length=len(bomb)
stack=[]
for a in s:
    stack.append(a)
    if a==bomb[-1] and ''.join(stack[-length:])==bomb:
        del stack[-length:]

print(''.join(stack)) if len(stack)>0 else print('FRULA')
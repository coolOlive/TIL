import sys
input=sys.stdin.readline

# 스택_괄호

t = int(input())

def isvps(s):
    stack=[]
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(s[i])
        else:
            if(len(stack)!=0):
                stack.pop()
            else:
                return False
    return len(stack)==0

for _ in range(t):
    s=list(map(str,input().strip()))
    if isvps(s):
        print("YES")
    else:
        print("NO")
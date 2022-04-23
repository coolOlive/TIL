import sys
input=sys.stdin.readline

# 스택_오큰수/골드4

n=int(input())
num=list(map(int,input().split()))
stack=[]
ans=[-1]*n

for i in range(n):
    while stack and num[i]>num[stack[-1]]:
        ans[stack.pop()]=num[i]
    stack.append(i)


print(*ans) 
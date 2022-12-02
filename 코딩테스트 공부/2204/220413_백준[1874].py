# 스택_스택 수열/실버3

n=int(input())
nums=[int(input()) for i in range(n)]
stack=[]
ans=[]
cnt=1
flag=1

for a in nums:
    while cnt<=a:
        stack.append(cnt)
        ans.append('+')
        cnt+=1
        
    if a==stack[-1]:
        stack.pop()
        ans.append('-')
    else:
        flag=0
        break


if flag==1:
    for b in ans:
        print(b)
else:
    print("NO")
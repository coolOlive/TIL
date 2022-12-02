from collections import deque

# bfs,dfs/숨바꼭질/실버1

def bfs(n):
    que.append(n)
    while que:
        a=que.popleft()
        if a==k:
            return (move[k])
        for i in (a-1,a+1,a*2):
            if 0<=i<=100000 and move[i]==0:
                move[i]=move[a]+1
                que.append(i)

n,k=map(int,input().split())
que=deque()
move=[0]*100001
print(bfs(n))
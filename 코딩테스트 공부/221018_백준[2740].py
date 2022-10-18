import sys
input=sys.stdin.readline

# 수학,구현/행렬 곱셈/실버5

n,m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m,k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]


for i in range(n):
    ans=[]
    for j in range(k):
        tmp=0
        for h in range(m):
            tmp+=a[i][h]*b[h][j]
        ans.append(tmp)
    print(*ans)
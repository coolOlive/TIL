# 구현,시뮬레이션_투명/실버5

img=[[0]*100 for _ in range(100)]

n,m=map(int,input().split())

for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    for a in range(x1,x2+1):
        for b in range(y1,y2+1):
            img[a-1][b-1]+=1
ans=0
for i in range(100):
    for j in range(100):
        if img[i][j]>m:
            ans+=1

print(ans)
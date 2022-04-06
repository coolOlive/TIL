import sys
input=sys.stdin.readline

# 브루트 포스_블랙잭/브론즈2

n,m=map(int,input().split())
black=list(map(int,input().split()))
balck_len = len(black)
ans = 0
for i in range(0, balck_len-2):
    for j in range(i+1, balck_len-1):
        for k in range(j+1, balck_len):
            if(black[i] + black[j] + black[k] > m):
                continue
            else:
                ans = max(ans ,black[i] + black[j] + black[k])

print(ans)

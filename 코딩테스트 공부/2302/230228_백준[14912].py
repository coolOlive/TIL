# 구현,브루트포스/숫자 빈도수/실버5

n,d = map(int,input().split())
d = str(d)
ans = 0

for i in range(1, n+1):
    if d in str(i):
        ans += str(i).count(d)

print(ans)

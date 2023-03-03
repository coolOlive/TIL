# 수학,그리디/박 터뜨리기/실버4

n,k = map(int, input().split())
bag = k*(k+1) // 2

if bag > n:
    print(-1)
elif (n - bag) % k == 0:
    print(k-1)
else:
    print(k)

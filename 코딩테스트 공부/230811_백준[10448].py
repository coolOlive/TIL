# 수학,브루트포스/유레카 이론/브론즈1
# 여행중

triangle = [n*(n+1)//2 for n in range(1, 46)]
ans = [0] * 1001

for i in triangle:
    for j in triangle:
        for k in triangle:
            if i+j+k <= 1000:
                ans[i+j+k] = 1

t = int(input())
for _ in range(t):
    print(ans[int(input())])

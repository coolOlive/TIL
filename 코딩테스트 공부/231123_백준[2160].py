import sys
input=sys.stdin.readline

# 브루트포스,수학/그림 비교/브론즈1

n=int(input())
picture=[list(input().strip() for _ in range(5)) for __ in range(n)]
mini,ans1,ans2 = 36,0,0

for i in range(n-1):
  for j in range(i+1,n):
    cnt = 0
    for k in range(5):
      for r in range(7):
        if picture[i][k][r] != picture[j][k][r]:
          cnt += 1
    if mini>cnt:
      ans1,ans2 = i+1,j+1
      mini = cnt
            

print(ans1,ans2)

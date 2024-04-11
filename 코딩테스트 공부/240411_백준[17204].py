import sys
input = sys.stdin.readline

# 구현,그래프이론/죽음의 게임/실버3
# 그래프로 다시 풀어봐야겠다!!

n,k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
now,ans = 0,0

for i in range(n):
  nextP = nums[now]
  ans += 1
  if nextP == k:
    print(ans)
    break
  now = nextP
else:
  print(-1)

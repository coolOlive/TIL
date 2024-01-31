# 브루트포스,정렬/Q-인덱스/실버5

n = int(input())
nums = sorted(list(map(int, input().split())))

for k in range(n,-1,-1):
  if k <= nums[-k]:
    print(k)
    break

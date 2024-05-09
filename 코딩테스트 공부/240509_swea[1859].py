# 백만 장자 프로젝트/D2

T = int(input())

for test_case in range(1, T + 1):
  n = int(input())
  cost = list(map(int,input().split()))
  max_v = cost[-1]
  ans = 0
  
  for i in range(n-1,-1,-1):
    now = cost[i]
    if max_v>now:
      ans += (max_v-now)
    else:
      max_v = now

  print('#{} {}'.format(test_case,ans))

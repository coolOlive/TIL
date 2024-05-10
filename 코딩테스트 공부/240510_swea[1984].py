# 중간 평균값 구하기/D2

T = int(input())

for t in range(1,T+1):
  nums = sorted(list(map(int,input().split())))
  ans = sum(nums[1:-1])/(len(nums)-2)
  print('#{} {}'.format(t,round(ans)))

# 정렬/최댓값과 최솟값/L2

def solution(s):
  nums=sorted(list(map(int,s.split())))
  return ' '.join([str(nums[0]),str(nums[-1])])

# 수학,이분탐색/제곱근/실버4

n = int(input())
l,r = 1,n

while 1:
  mid = (l + r) // 2
  tmp = mid**2
  if tmp == n:
    print(mid)
    break
  elif tmp < n:
    l = mid+1
  else:
    r = mid - 1

# 수학/2로 몇 번 나누어질까/골드4

a,b = map(int,input().split())

def cal(n):
  cnt = n
  tmp = 2
  while tmp<=n:
    cnt += (n//tmp)*(tmp//2)
    tmp*=2
  return cnt

print(cal(b)-cal(a-1))
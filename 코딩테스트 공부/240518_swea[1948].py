# 자료구조/날짜 계산기/D2

T = int(input())

last = [0,31,28,31,30,31,30,31,31,30,31,30,31]

for t in range(1,T+1):
  m1,d1,m2,d2 = map(int,input().split())
  ans = (d2 + last[m1] - d1) + 1
  if m1==m2:
    ans = d2-d1+1
    print('#{} {}'.format(t,ans))
    continue
  
  for i in range(m1+1,m2):
    ans += last[i]

  print('#{} {}'.format(t,ans))

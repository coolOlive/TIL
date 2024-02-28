# 구현/반올림/브론즈1

n = int(input())

for _ in range(n):
  tmp = list(input())
  for i in range(len(tmp)-1,0,-1):
    if int(tmp[i])>=5:
      tmp[i-1] = str(int(tmp[i-1])+1)
    tmp[i] = '0'

  for t in tmp:
    print(t,end='')
  
  print()

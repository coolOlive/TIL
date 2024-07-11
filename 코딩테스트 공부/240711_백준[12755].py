# 수학,브루트포스/수면 장애/s4
# 아니..이거 시간 너무 걸려서 결국 찾아서 풀었다.

n = int(input())
largest,prev=9,9
line = 2
ten = 1

if(n<10):
  print(n)
else:
  while(1):
    largest += 9*(10**ten)*line
    if(prev < n and largest >= n):
      break
    line+=1
    ten+=1
    prev=largest

  count = (n-(prev+1)) // line
  num = str((10**(line-1)) + count)
  loca = (n-(prev+1)) % line
  print(num[loca])
  
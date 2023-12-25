import sys
input = sys.stdin.readline

# 구현/아스키 아트/브론즈1

n,m = map(int,input().split())

def img(r,g,b):
  tmp = 2126 * r + 7152 * g + 722 * b

  if 0 <= tmp < 510000:
    return '#'
  if 510000 <= tmp < 1020000:
    return 'o'
  if 1020000 <= tmp < 1530000:
    return '+'
  if 1530000 <= tmp < 2040000:
    return '-'
  return '.'
  
for i in range(n):
  line = list(map(int,input().split()))
  ans = []
  
  for j in range(0, len(line) - 2, 3):
    ans.append(img(line[j], line[j+1], line[j+2]))
  print(''.join(ans))

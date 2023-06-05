import sys
input=sys.stdin.readline

# 정렬,브루트포스/십자카드 문제/실버3

nums = list(map(int,input().split()))

def clock(n):
  small = int(''.join(map(str, n)))
  for i in range(1,4):
    tmp = int(''.join(map(str, n[i:]+n[:i])))
    if small > tmp:
      small = tmp
  return small

cn = clock(nums)
cnt = 1

for i in range(1111, cn):
  tmp = list(str(i))
  if '0' not in tmp:
    if i == clock(list(map(int, str(i)))):
      cnt += 1

print(cnt)

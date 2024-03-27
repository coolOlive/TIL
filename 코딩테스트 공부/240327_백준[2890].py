import re
import sys
input = sys.stdin.readline

# 문자열,구현/카약/실버5

r,c = map(int,input().split())
cnt = [-1]*9
dic = dict()
rank = 1

for _ in range(r):
  boat = re.split("[1-9]{2}", input().strip())
  if boat[0].count('.') != (c-2):
      cnt[int(boat[1][0])-1] = ((c-5) - boat[0].count('.'))

for a in sorted(cnt):
  if a not in dic:
    dic[a] = rank
    rank += 1
ans = [dic[i] for i in cnt]

for a in ans:
  print(a)

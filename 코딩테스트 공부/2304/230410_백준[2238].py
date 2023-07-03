from collections import defaultdict
import sys
input=sys.stdin.readline

# 구현/경매/실버5

u,n = map(int,input().split())
price = defaultdict(list)
cnt = defaultdict(int)
pList = set([])

for _ in range(n):
  name, p = input().split()
  p = int(p)
  pList.add(p)
  price[p].append(name)
  cnt[p] += 1

smallPeopleNum = min(cnt.values())
pList = sorted(list(pList))

for a in pList:
  if cnt[a] == smallPeopleNum:
    print(price[a][0],a)
    break

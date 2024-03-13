import sys
input=sys.stdin.readline

# 구현,브루트포스/아이폰 9S/실버4

n = int(input())
bs = [int(input()) for _ in range(n)]
bite = set(bs)
ans = 0

for b in bite:
  cnt = 1
  tmp = [x for x in bs if x!=b]

  for i in range(len(tmp)-1):
    if tmp[i]==tmp[i+1]:
      cnt += 1
    else:
      ans = max(ans,cnt)
      cnt = 1

  ans = max(ans,cnt)

print(ans)

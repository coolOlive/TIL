import sys
input=sys.stdin.readline

# 구현/기술 연계마스터 임스/실버5

n = int(input())
skills = list(input().strip())
ans = 0
rl = 0
sk = 0

for s in skills:
  if s =='L':
    rl += 1
  elif s=='R':
    if rl>0:
      ans += 1
      rl -= 1
    else:
      break
  elif s=='S':
    sk += 1
  elif s=='K':
    if sk>0:
      ans += 1
      sk -= 1
    else:
      break
  else:
    ans += 1

print(ans)

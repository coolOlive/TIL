import sys
input = sys.stdin.readline

# 구현/농구 경기/브론즈2

n = int(input())
names,ans = [],[]

for _ in range(n):
  tmp = input()
  names.append(tmp[0])

setNames = set(names)

for name in setNames:
  if names.count(name) >= 5:
    ans.append(name)
      
ans = sorted(ans)

if len(ans) > 0:
  print(''.join(ans))
else:
  print("PREDAJA")

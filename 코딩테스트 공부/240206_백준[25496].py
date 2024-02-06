import sys
input=sys.stdin.readline

# 그리디/장신구 명장 임스/실버5

p, n = map(int, input().split())
deco = sorted(list(map(int, input().split())))
ans = 0

for i in range(n):
  if p < 200:
    p += deco[i]
    ans += 1
    continue
  break
        
print(ans)

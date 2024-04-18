from collections import defaultdict
import sys
input=sys.stdin.readline

# 자료구조,해시/평행선/실버4

n = int(input())
x = defaultdict(list)
y = defaultdict(list)
ans = 0

for _ in range(n):
  a, b = map(int, input().split())
  x[a].append(b)
  y[b].append(a)

for a in x:
  if len(x[a]) >= 2:
    ans += 1
    
for b in y:
  if len(y[b]) >= 2:
    ans += 1

print(ans)

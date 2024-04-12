import sys
input = sys.stdin.readline

# 자료구조,해시/I AM IRONMAN/실버3

n,p = map(int, input().split())
w,l,g = map(int, input().split())
player = {}
score = 0
ans = "I AM IRONMAN!!"

for _ in range(p):
  a,b = map(str, input().split())
  player[a] = b

for i in range(n):
  match = input().strip()
  if match not in player or player[match]=='L':
    score -= l
    if score<=0:
      score = 0
    continue
  score += w
  if score >= g:
    ans = "I AM NOT IRONMAN!!"
    break

print(ans)

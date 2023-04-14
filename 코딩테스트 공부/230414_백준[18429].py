from itertools import permutations
import sys
input=sys.stdin.readline

# 조합,백트래킹,브루트포스/근손실/실버3

n,k= map(int,input().split())
health = list(map(int,input().split()))
health = list(permutations(health,n))
ans = 0

for kits in health:
  weight = 500
  for kit in kits:
    if weight+kit-k < 500:
      break
    else:
      weight = weight+kit-k
  else:
    ans += 1

print(ans)

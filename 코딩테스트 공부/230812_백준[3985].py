import sys
input=sys.stdin.readline

# 구현/롤 케이크/브론즈1
# 여행중

L = int(input().strip())
cake = [0] * (L + 1)
n = int(input().strip())
audience = [0] * (n + 1)
M_idx, M_cnt = 0, 0

for i in range(1, n + 1):
  P, K = map(int, input().split())
  if K - P - 1 > M_cnt:
    M_idx = i
    M_cnt = K-P-1
  cnt = 0
  for j in range(P, K + 1):
    if not cake[j]:
      cake[j] = 1
      cnt += 1
  audience[i] = cnt

print(M_idx)
print(audience.index(max(audience)))

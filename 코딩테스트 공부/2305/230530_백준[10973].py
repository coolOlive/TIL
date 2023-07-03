import sys
input = sys.stdin.readline

# 수학,조합론,구현/이전 순열/실버3

n = int(input())
a = list(map(int, input().split()))

for i in range(n-1, 0, -1):
  if a[i] < a[i-1]:
    for j in range(n-1, 0, -1):
      if a[j] < a[i-1]:
        a[j], a[i-1] = a[i-1], a[j]
        a = a[:i] + sorted(a[i:], reverse=True)
        print(*a)
        exit()

print(-1)

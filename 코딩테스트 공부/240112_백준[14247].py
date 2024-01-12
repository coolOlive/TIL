import sys
input=sys.stdin.readline

# 구현,그리디/나무 자르기/실버2

n = int(input())
h = list(map(int,input().split()))
growth = list(map(int,input().split()))
ans = 0
tree = []

for i in range(n):
  tree.append([h[i],growth[i]])
tree.sort(key = lambda x:x[1])

for i in range(n):
  ans += tree[i][0] + ( i*tree[i][1])

print(ans)

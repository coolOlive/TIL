import sys
input=sys.stdin.readline

# 그리디/우리집엔 도서관이 있어/실버2

n = int(input())
books = [int(input()) for _ in range(n)]
position,ans = n,0

for i in range(n-1, -1, -1):
  if books[i] != position:
    ans += 1
  else:
    position -= 1

print(ans)

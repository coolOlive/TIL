import sys
input=sys.stdin.readline

# 구현/자료구조는 정말 최고야/실버5

n,m = map(int,input().split())
ans = 'Yes'

for i in range(m):
  cnt = int(input())
  books = list(map(int,input().split()))
  tmp = sorted(books,reverse = True)
  if books != tmp:
    ans = 'No'
    break

print(ans)

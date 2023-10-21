import sys
input=sys.stdin.readline

# 구현/바구니 뒤집기/브론즈2
# 시험기간이라 한동안 쉬운 문제 풀 예정

n,m = map(int, input().split())
box = [i for i in range(1,n+1)]
tmp = 0

for x in range(m):
  i,j = map(int, input().split())
  tmp = box[i-1:j]
  tmp.reverse()
  box[i-1:j] = tmp

for x in range(n):
  print(box[x],end=' ')

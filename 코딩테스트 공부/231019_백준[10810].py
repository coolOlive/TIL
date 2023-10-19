# 구현/공 넣기/브론즈3
# 시험기간이라 한동안 쉬운 문제 풀 예정

n,m = map(int, input().split())
box = [0] * (n+1)

for _ in range(m):
  i, j, k = map(int, input().split())
  for idx in range(i, j+1):
    box[idx] = k

for i in range(1, n+1):
  print(box[i], end = ' ')

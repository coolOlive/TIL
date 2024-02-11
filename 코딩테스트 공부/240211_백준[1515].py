import sys
input=sys.stdin.readline

# 그리디/수 이어 쓰기/실버3

num = input().strip()
n, idx = 0,0
flg = 1

while 1:
  n += 1
  for s in str(n):
    if num[idx]==s:
      idx += 1
      if idx>= len(num):
        print(n)
        flg = 0
        break
  if not flg:
    break

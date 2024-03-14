import sys
input = sys.stdin.readline

# 구현,수학/영식이의 손가락/실버3

f = int(input())
cnt = int(input())
ans = 0

if f==1:
  ans = cnt*8
elif f==5:
  ans = cnt*8+4
else:
  if cnt % 2 == 0:
    ans = cnt*4 + (f-1)
  else:
    ans = cnt*4 + (5-f)

print(ans)

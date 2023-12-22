import sys
input = sys.stdin.readline

# 구현,정렬/6174/브론즈1

n = int(input())

for _ in range(n):
  num = int(input())
  cnt = 0
  while num != 6174:
    cnt += 1
    tmp1 = sorted(list(str(num)),reverse = True)
    tmp2 = tmp1[::-1]
    num = int(''.join(tmp1))-int(''.join(tmp2))
    if len(str(num)) < 4:
      strNum = str(num) + ('0')*(4-len(str(num)))
      num = int(strNum)

  print(cnt)

import sys
input = sys.stdin.readline

# 그리디/당신은 운명을 믿나요?/브론즈1

korea = 'KOREA'
yonsei = 'YONSEI'

k = 0
y = 0

s = input()

for i in s:
  if i == korea[k] and i == yonsei[y]:
    k+=1
    y+=1
  elif i == korea[k]:
    k+=1
  elif i == yonsei[y]:
    y+=1

  if k==5:
    print(korea)
    break
  elif y==6:
    print(yonsei)
    break

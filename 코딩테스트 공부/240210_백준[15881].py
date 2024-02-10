import sys
input=sys.stdin.readline

# 그리디/Pen Pineapple Apple Pen/브론즈1

n = int(input())
app = input().strip()
tmp = [1]*n
ans = 0

for i in range(len(app)-3):
  if app[i:4+i] == 'pPAp':
    if sum(tmp[i:4+i])== 4:
      tmp[i] = 0
      tmp[i+3] = 0
      ans += 1

print(ans)

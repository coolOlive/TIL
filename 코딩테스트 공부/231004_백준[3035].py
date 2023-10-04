import sys
input=sys.stdin.readline

# 구현,문자열/스캐너/브론즈1

r,c,zr,zc = map(int, input().split())
words = [input().strip() for _ in range(r)]
ans = []

for i in range(r):
  tmp = ''
  for j in range(c):
    tmp+=str(words[i][j]*zc)
  for _ in range(zr):
    ans.append(tmp)

print(*ans,sep='\n')

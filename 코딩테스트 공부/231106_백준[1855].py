import sys
input = sys.stdin.readline

# 구현/암호/브론즈1

n = int(input())
s = input().strip()
line = len(s)//n
box = [list(s[i:i+n]) for i in range(0,len(s),n)]
ans = ''

for i in range(line):
  if i%2!=0:
    box[i].reverse()

for i in range(n):
  for j in range(line):
    ans += box[j][i]
        
print(ans)
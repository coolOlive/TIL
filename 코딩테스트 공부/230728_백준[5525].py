# 문자열/IOIOI/실버1

n = int(input())
m = int(input())
s = input()

loca,cnt,ans = 0,0,0

while loca < (m - 1):
  if s[loca:loca + 3] == 'IOI':
    loca += 2
    cnt += 1
    if cnt == n:
      ans += 1
      cnt -= 1
  else:
    loca += 1
    cnt = 0

print(ans)

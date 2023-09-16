import sys
input=sys.stdin.readline

# dp,구현/핸드폰 번호 궁합/브론즈1

a = list(map(int, input().strip()))
b = list(map(int, input().strip()))
ans = []

for i in range(8):
  ans.append(a[i])
  ans.append(b[i])

while len(ans)!=2:
  tmp = []
  for i in range(len(ans)-1):
    tmp.append((ans[i]+ans[i+1])%10)
  ans = tmp

print(*ans,sep='')

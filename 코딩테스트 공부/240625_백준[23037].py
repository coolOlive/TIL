import sys
input=sys.stdin.readline

# 구현/5의 수난/브론즈2

num = input().strip()
ans=0

for i in range(len(num)):
  ans+= int(num[i])**5

print(ans)

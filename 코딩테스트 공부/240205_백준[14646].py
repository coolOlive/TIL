import sys
input=sys.stdin.readline

# 구현/욱제는 결정장애야!!/실버5

n = int(input())
nums = list(map(int, input().split()))
menu = []
ans,cnt = 0,0

for num in nums:
  if num not in menu:
    menu.append(num)
    cnt+=1
  else:
    cnt-=1
  ans = max(ans,cnt)

print(ans)

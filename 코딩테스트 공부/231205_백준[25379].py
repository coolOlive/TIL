import sys
input=sys.stdin.readline

# 그리디/피하자/실버4

n = int(input())
aList = list(map(int, input().split()))
ans1, ans2, plus = 0, 0, 0

for a in aList:
  if a%2==1:
    plus += 1
  else:
    ans1 += plus
      
aList.reverse()
plus = 0

for a in aList:
  if a%2==1:
    plus += 1
  else:
    ans2 += plus
      
print(min(ans1, ans2))

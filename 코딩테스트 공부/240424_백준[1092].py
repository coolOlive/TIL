import sys
input=sys.stdin.readline

# 그리디,정렬/배/골드5

n = int(input())
crane = list(map(int,input().split()))
m = int(input())
box = list(map(int,input().split()))
ans = 0

crane.sort(reverse = True)
box.sort(reverse = True)

if crane[0] < box[0]:
  ans = -1
else:
  while len(box) > 0:
    for c in crane:
      for b in box:
        if c >= b:
          box.remove(b)
          break
    ans += 1

print(ans)

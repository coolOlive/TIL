import sys
input = sys.stdin.readline

# 자료구조/트럭/실버1

n, w, l = map(int, input().split())
car = list(map(int, input().split()))
road = [0] * w
ans = 0
 
while road:
  road.pop(0)
  if car:
    tmp = sum(road) + car[0]
    if tmp <= l:
      road.append(car.pop(0))
    else:
      road.append(0)
  ans += 1

print(ans)

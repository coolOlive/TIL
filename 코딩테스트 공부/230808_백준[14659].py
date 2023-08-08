# 그리디/한조서열정리하고옴ㅋㅋ/브론즈1
# 여행중

n = int(input())
arr = list(map(int,input().split()))

high, cnt = 0, 0
ans = []

for i in arr:
  if i > high:
    high = i
    cnt = 0
  else:
    cnt += 1
  ans.append(cnt)

print(max(ans))

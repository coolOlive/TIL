import sys
input=sys.stdin.readline

# 자료구조,스택/과제는 끝나지 않아!/실버3

n = int(input())
work = []
ans = 0

for _ in range(n):
  new = list(map(int,input().split()))
  if new[0] == 1:
    work.append([new[1],new[2]])

  if work:
    score,time = work.pop()
    time -= 1
    if time == 0:
      ans += score
    else:
      work.append([score,time])

print(ans)

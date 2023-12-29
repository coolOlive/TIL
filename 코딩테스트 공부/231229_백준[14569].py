import sys
input=sys.stdin.readline

# 구현/시간표 짜기/실버2

n = int(input().strip())
classL = []
student = []

for _ in range(n):
  tmp = list(map(int, input().split()))
  classL.append(set(tmp[1:]))
  
m = int(input().strip())
for _ in range(m):
  tmp = list(map(int, input().split()))
  student.append(set(tmp[1:]))

for s in student:
  ans = 0
  for c in classL:
    if s&c == c:
      ans += 1
  print(ans)

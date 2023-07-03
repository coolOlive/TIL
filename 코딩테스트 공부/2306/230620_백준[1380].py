import sys
input = sys.stdin.readline

# 구현,문자열/귀걸이/실버5

idx = 1

while True:
  n = int(input())
  if n==0:
    break
  student = dict()
  for i in range(n):
    student[i+1] = [input().strip(),0]
  
  for j in range(2*n-1):
    a,b = map(str, input().split())
    student[int(a)][1] += 1

  for st in student.values():
    if st[1]==1:
      print(idx,st[0])
      break
  idx += 1

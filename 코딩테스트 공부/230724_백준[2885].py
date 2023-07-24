import sys
input = sys.stdin.readline

# 수학,그리디/초콜릿 식사/실버2
# 문제 이해가 어려웠던 문제

k = int(input())
size = 1
cut = 0

while size < k:
  size *= 2

print(size,end = ' ')

while 1:
  if k%size != 0:
    size //= 2
    cut += 1
  else:
    print(cut)
    break

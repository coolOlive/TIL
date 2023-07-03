import sys
input = sys.stdin.readline

# 수학,정렬,그리디/삼각형 만들기/실버3

n = int(input())
straw = [int(input()) for _ in range(n)]
straw.sort(reverse = True)

for i in range(n-2):
  a,b,c = straw[i],straw[i+1],straw[i+2]
  if b+c > a:
    print(a+b+c)
    break
else:
  print(-1)

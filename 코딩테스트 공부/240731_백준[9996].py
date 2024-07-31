import sys
input=sys.stdin.readline

# 문자열/한국이 그리울 땐 서버에 접속하지/실버3

n = int(input())
x,y = input().split("*")
L = len(x) + len(y)

for _ in range(n):
  file = input()
  if L<=len(file) and x == file[:len(x)] and y == file[-len(y):]:
    print("DA")
  else:
    print("NE")

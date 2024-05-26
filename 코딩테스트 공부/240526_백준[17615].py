import sys
input=sys.stdin.readline

# 그리디/볼 모으기/실버1

n = int(input())
balls = input().strip()

def left(color):
  return (balls.lstrip(color)).count(color)

def right(color):
  return (balls.rstrip(color)).count(color)

ans = min(left('R'),left('B'),right('R'),right('B'))
print(ans)

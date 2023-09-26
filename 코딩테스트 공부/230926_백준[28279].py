import sys
input=sys.stdin.readline
from collections import deque

# 자료구조/덱 2/실버4

n = int(input())
q = deque()

def one(x):
  q.appendleft(x)
  
def two(x):
  q.append(x)

def three():
  if len(q)==0:
    print(-1)
  else:
    print(q.popleft())

def four():
  if len(q)==0:
    print(-1)
  else:
    print(q.pop())

def five():
  print(len(q))

def six():
  if q:
    print(0)
  else:
    print(1)

def seven():
  if q:
    print(q[0])
  else:
    print(-1)

def eight():
  if q:
    print(q[-1])
  else:
    print(-1)

for _ in range(n):
  order = list(map(int,input().split()))
  if len(order) == 2:
    if order[0] == 1:
      one(order[1])
      continue
    two(order[1])
  elif order[0] == 3:
    three()
  elif order[0] == 4:
    four()
  elif order[0] == 5:
    five()
  elif order[0] == 6:
    six()
  elif order[0] == 7:
    seven()
  elif order[0] == 8:
    eight()

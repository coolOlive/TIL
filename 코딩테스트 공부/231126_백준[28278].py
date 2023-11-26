import sys
input = sys.stdin.readline

# 스택,자료구조/스택 2/실버4

n = int(input())
stack = []

for _ in range(n):
  order = input().rstrip()
  
  if len(order) > 2:
    stack.append(int(order[2:]))
      
  elif order == '2':
    if len(stack)==0:
      print(-1)
    else:
      print(stack.pop())

  elif order == '3':
    print(len(stack))
      
  elif order == '4':
    if len(stack)==0:
      print(1)
    else:
      print(0)
  
  elif order == '5':
    if len(stack)==0:
      print(-1)
    else:
      print(stack[-1])

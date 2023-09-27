import sys
input=sys.stdin.readline

# 자료구조/철벽 보안 알고리즘/실버4

t = int(input())

for _ in range(t):
  dic = {}
  n = int(input())
  op1 = list(input().split())
  op2 = list(input().split())
  pw = list(input().split())
  
  for i in op2:
    dic[op1.index(i)] = pw.pop(0)
  
  print(' '.join(dict(sorted(dic.items())).values()))

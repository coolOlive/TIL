import sys
input = sys.stdin.readline

# 수학,구현,정렬/solved.ac/실버4

n = int(input())

def rnd(num):
  return int(num)+[0, 1][num - int(num) >= 0.5]

if n==0:
  print(0)
else:
  rank = [int(input()) for _ in range(n)]
  rank = sorted(rank)
  people = rnd(n*0.15)
  if people>0:
    rank = rank[people:-people]
  print(rnd(sum(rank)/(n-people*2)))

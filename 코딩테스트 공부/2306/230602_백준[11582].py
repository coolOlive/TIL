import sys
input=sys.stdin.readline

# 정렬,분할정복/치킨 TOP N/실버4

n = int(input())
chicken = list(map(int, input().split()))
k = int(input())
idx = n // k

for i in range(0,n,idx):
  score = chicken[i:i+idx]
  score.sort()
  print(*score, end = ' ')

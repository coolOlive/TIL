import sys
from queue import PriorityQueue
input = sys.stdin.readline

# 구현/여우 사인/실버5

n = int(input())
hand = [[] for _ in range(6)]
ans = 'Wa-pa-pa-pa-pa-pa-pow!'

for _ in range(n):
  a,b = map(int,input().split())
  hand[a].append(b)
  hand[b].append(a)

if 3 and 4 not in hand[1]:
  ans = 'Woof-meow-tweet-squeek'
elif 1 and 4 not in hand[3]:
  ans = 'Woof-meow-tweet-squeek'
elif 1 and 3 not in hand[4]:
  ans = 'Woof-meow-tweet-squeek'
elif len(hand[1])!=2 or len(hand[3])!=2 or len(hand[4])!=2:
  ans = 'Woof-meow-tweet-squeek'

print(ans)

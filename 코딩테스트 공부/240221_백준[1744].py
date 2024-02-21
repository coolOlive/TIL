import sys
from queue import PriorityQueue
input = sys.stdin.readline

# 그리디/수 묶기/골드4

n = int(input())
minus = PriorityQueue()
plus = PriorityQueue()
zero, one = 0, 0

for _ in range(n):
  num = int(input())
  if num<0:
    minus.put(num)
    continue
  if num==0:
    zero += 1
    continue
  if num==1:
    one += 1
    continue
  plus.put(num*-1)

ans = one

while plus.qsize()>1:
  a = plus.get()*-1
  b = plus.get()*-1
  ans += a*b

if plus.qsize()>0:
  ans += plus.get()*-1

while minus.qsize()>1:
  a = minus.get()
  b = minus.get()
  ans += a*b

if minus.qsize()>0 and zero==0:
  ans += minus.get()

print(ans)

import sys
input=sys.stdin.readline

# 구현,재귀/222-풀링/실버2

n=int(input())
nums=[list(map(int, input().split())) for _ in range(n)]

def ttt(size, x, y):
  mid=size//2
  
  if size == 2:
    ans=[nums[x][y], nums[x+1][y], nums[x][y+1], nums[x+1][y+1]]
    ans.sort()
    return ans[-2]

  lt=ttt(mid, x, y)
  rt=ttt(mid, x+mid, y)
  lb=ttt(mid, x, y+mid)
  rb=ttt(mid, x+mid, y+mid)
  ans=[lt, rt, lb, rb]
  ans.sort()
  return ans[-2]

print(ttt(n, 0, 0))

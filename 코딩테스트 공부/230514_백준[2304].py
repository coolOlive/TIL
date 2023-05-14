import sys
input = sys.stdin.readline

# 브루트포스,자료구조/창고 다각형/실버2

n = int(input())

sticks = dict()
loca = []
largest = 0
largestLoca = 0
largestIdx = 0
ans = 0

for _ in range(n):
  a,b = map(int,input().split())
  sticks[a] = b
  loca.append(a)
  if largest < b:
    largest = b
    largestLoca = a

loca.sort()
largestIdx = loca.index(largestLoca)

height = sticks[loca[0]]

for i in range(largestIdx):
  if height < sticks[loca[i]]:
    height = sticks[loca[i]]
    ans += height*(loca[i+1]-loca[i])
  else:
    ans += height*(loca[i+1]-loca[i])
        
height = sticks[loca[-1]]

for i in range(n-1,largestIdx,-1):
  if height < sticks[loca[i]]:
    height = sticks[loca[i]]
    ans += height*(loca[i]-loca[i-1])
      
  else:
    ans += height*(loca[i]-loca[i-1])

print(ans+largest)

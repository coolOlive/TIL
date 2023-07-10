import sys
input=sys.stdin.readline

# 구현/줄세우기/실버5
# 쏘 비지

p = int(input())  
arr = [list(map(int, input().split())) for _ in range(p)]  
height = [[] for _ in range(p)]
ans = [[] for _ in range(p)]
cnt = 0

for i in range(p):
  cnt=0
  height[i].append(arr[i][0])
  height[i].append(arr[i][1])
  for j in range(2, 21):  
    for k in range(1, len(height[i])):
      if (arr[i][j] < height[i][k]): 
        height[i].insert(k, arr[i][j])
        cnt += len(height[i]) - 1 - k
        break
      if k == len(height[i]) - 1: 
        height[i].append(arr[i][j]) 
  ans[i].append(arr[i][0]) 
  ans[i].append(cnt)   

for i in range(p):
  print(ans[i][0], ans[i][1])

import sys
input = sys.stdin.readline

# 기하학/다각형의 면적/골드5

n = int(input())
x,y = [],[]

for _ in range(n):
  a,b = map(int,input().split())
  x.append(a)
  y.append(b)

x.append(x[0])
y.append(y[0])

a,b = 0,0

for i in range(n):
  a += x[i]*y[i+1]
  b += y[i]*x[i+1]
    
print(round(abs((a-b)/2),1))

import math

# 수학/당근 키우기/실버4

x, y = map(int, input().split())
print(math.trunc(x+y+(min(x,y)/10)))

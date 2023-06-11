import math
import sys
input = sys.stdin.readline

# 수학/조약돌 꺼내기/실버3

m = int(sys.stdin.readline())
colors = list(map(int,input().split()))
k = int(input())
n = sum(colors)
total = math.comb(n,k)
same = 0

for color in colors:
  same += math.comb(color,k)

print(same/total)

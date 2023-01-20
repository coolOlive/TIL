import bisect
import sys
input=sys.stdin.readline

# 이분탐색/IF문 좀 대신 써줘/실버3
# bisect을 알게 됨

n,m = map(int,input().split())
name = []
count = [-1]

for _ in range(n):
    a,b = input().split()
    name.append(a)
    count.append(int(b))
    
for _ in range(m):
    num = int(input())
    index = bisect.bisect_left(count, num)
    print(name[index - 1])


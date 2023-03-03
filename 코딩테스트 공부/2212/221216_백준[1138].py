import sys
input=sys.stdin.readline

# 구현/한 줄로 서기/실버2

n = int(input())
height = list(map(int,input().split()))
seat = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == height[i] and seat[j] == 0:
            seat[j] = str(i+1)
            break
        elif seat[j] == 0:
            cnt+=1

print(' '.join(seat))
import sys
input=sys.stdin.readline

# 수학, 기하학_직사각형에서 탈출/브론즈3

x,y,w,h=map(int,input().split())
dist=[x,y,w-x,h-y]
print(min(dist))
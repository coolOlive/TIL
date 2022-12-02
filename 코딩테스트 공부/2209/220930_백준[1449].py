import sys
input=sys.stdin.readline

 # 그리디,정렬/수리공 항승/실버3

n,l=map(int,input().split())
water=list(map(int,input().split()))

water.sort()

cnt=1
tmp=water[0]

for w in water[1:]:
    if w<tmp or w>=tmp+l:
        tmp=w
        cnt+=1

print(cnt)
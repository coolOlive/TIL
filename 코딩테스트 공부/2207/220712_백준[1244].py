import sys
input=sys.stdin.readline

# 구현,시뮬레이션_스위치 켜고 끄기/실버3

size=int(input())
switch=list(map(int,input().split()))

onoff={1:0,0:1}

def man(num):
    for i in range(num-1,len(switch),num):
        switch[i]=onoff[switch[i]]

def woman(num):
    l,r=num-2,num
    while l>=0 and r<len(switch):
        if switch[l]==switch[r]:
            switch[l]=onoff[switch[l]]
            switch[r]=onoff[switch[r]]
        else:
            break
        l-=1
        r+=1

n=int(input())
for _ in range(n):
    gender,num=map(int,input().split())
    if gender==1:
        man(num)
    else:
        switch[num-1]=onoff[switch[num-1]]
        woman(num)
        
count=0
while count < len(switch):
    print(switch[count], end=" ")
    if count % 20 == 19:
        print()
    count += 1
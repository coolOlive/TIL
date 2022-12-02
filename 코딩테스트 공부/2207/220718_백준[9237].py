# 그리디_이장님 초대/실버5

n=int(input())
trees=list(map(int,input().split()))
trees.sort(reverse=True)

dday=1
now=2

for tree in trees:
    if now+tree>dday:
        dday=now+tree
    now+=1

print(dday)
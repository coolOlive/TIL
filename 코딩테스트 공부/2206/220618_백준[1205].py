# 구현_등수 구하기/실버5


n,score,p=map(int,input().split())
if n==0:
    print(1)
else:
    rank=sorted(list(map(int,input().split()))+[score], reverse=True)
    if rank.index(score)+rank.count(score)>p:
        print(-1)
    else:
        print(rank.index(score)+1)
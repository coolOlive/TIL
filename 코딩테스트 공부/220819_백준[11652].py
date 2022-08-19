import sys
input=sys.stdin.readline

# 해시,정렬/카드/실버4

n=int(input())
card={}

for _ in range(n):
    tmp=int(input())
    if tmp in card:
        card[tmp]+=1
    else:
        card[tmp]=0

ans=sorted(card.items(),key=lambda x : (-x[1],x[0]))
print(ans[0][0])
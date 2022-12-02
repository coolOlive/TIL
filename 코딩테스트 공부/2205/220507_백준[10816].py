import sys
input=sys.stdin.readline

# 자료구조, 정렬, 이분 탐색_숫자 카드2/실버4
# 해쉬 알고리즘을 더 공부해야겠다./ 내가 푼 방법은 시간이 너무 오래 걸려

n=int(input())
card=sorted(list(map(int,input().split())))

m=int(input())
num=list(map(int,input().split()))

cnt={}
for c in card:
    if c in cnt:
        cnt[c]+=1
    else:
        cnt[c]=1

ans=[0]*m

for i in range(m):
    start,last=0,n-1
    while start<=last and i<m:
        mid=(start+last)//2
        tmp=num[i]
        
        if tmp < card[mid]:
            last=mid-1
        elif tmp > card[mid]:
            start=mid+1
        else:
            ans[i]=cnt.get(tmp)
            break

for a in ans:
    print(a,end=' ')
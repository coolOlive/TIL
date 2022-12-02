# 수학,브루트포스,정렬_좋은 구간/실버5

l=int(input())
s=sorted([0]+list(map(int,input().split())))
n=int(input())

ans=0

for i in range(l):
    if n==s[i] or n==s[i+1]:
        break
    elif s[i]<n and n<s[i+1]:
        ans=(n-s[i])*(s[i+1]-n)-1
        break
print(ans)
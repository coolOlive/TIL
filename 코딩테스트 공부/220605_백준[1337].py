import sys
input=sys.stdin.readline

# 구현,정렬,두 포인터_올바른 배열/실버4

n=int(input())
nums=[]
ans=5

for _ in range(n):
    nums.append(int(input()))
nums.sort()


for i in range(n):
    cnt1,cnt2=4,4
    for j in range(n):
        if nums[i]+5 > nums[j] and i<j:
            cnt1-=1
        elif nums[i]-5 < nums[j] and i>j:
            cnt2-=1
    ans=min(ans,cnt1,cnt2)
        

print(ans)
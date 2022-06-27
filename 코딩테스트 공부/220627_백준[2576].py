import sys
input=sys.stdin.readline

# 수학,구현_홀수/브론즈3

nums=[]

for _ in range(7):
    tmp=int(input())
    if tmp%2==1:
        nums.append(tmp)


if len(nums)>0:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)

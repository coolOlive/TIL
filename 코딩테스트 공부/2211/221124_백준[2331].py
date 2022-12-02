# 구현/반복수열/실버4

a,p = map(int,input().split())
nums=[a]

while 1:
    tmp = 0
    for i in str(nums[-1]):
        tmp+=int(i)**p
    if tmp in nums:
        break
    nums.append(tmp)

print(nums.index(tmp))
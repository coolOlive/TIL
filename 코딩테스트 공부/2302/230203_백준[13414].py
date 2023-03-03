import sys
input=sys.stdin.readline

# 자료구조,해시/수강신청/실버3

k,l = map(int,input().split())
nums = dict()
cnt = 0

for i in range(l):
    student = input().strip()
    nums[student] = i

nums = sorted(nums.items(), key = (lambda x:x[1]))

for n in nums:
    if cnt == k:
        break
    print(n[0])
    cnt += 1

import sys
input=sys.stdin.readline

 # 수학,정수론/약수/브론즈1

n=int(input())
nums=list(map(int,input().split()))
nums.sort()

print(nums[0]*nums[-1])
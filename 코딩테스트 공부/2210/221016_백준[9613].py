import sys,math
input = sys.stdin.readline

# 유클리드호제법,수학/GCD 합/실버4

def gcd(n1,n2):
    while(True):
        k = n2 % n1
        if k == 0:
            return n1
        n2 = n1;
        n1 = k

for _ in range(int(input())):
    tmp = list(map(int,input().split()))
    n,nums,k = tmp[0],tmp[1:],0
    
    for i in range(n-1):
        for j in range(i+1,n):
            k += gcd(nums[i],nums[j])
    print(k)
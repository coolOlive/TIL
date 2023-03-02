# 에라토스테네스/수 복원하기/실버3

t = int(input())
nums = [int(input()) for _ in range(t)]
maxnum = max(nums)
primes = []
visit = [0,0]+[1]*(maxnum-1)

for i in range(2,maxnum+1):
    if visit[i]:
        primes.append(i)
        for j in range(2*i,maxnum+1,i):
            visit[j] = 0

for n in nums:
    for p in primes:
        cnt = 0
        if n%p == 0:
            while n%p == 0:
                n //= p
                cnt += 1
            print(p,cnt)
        elif n == 1:
            break
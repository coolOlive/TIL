a,b = map(int,input().split())
sosu = [False,False] + [True]*100001
nums = [0]*100002
now,ans = 0,0

# 에라토스테네스의체,소수판정/언더프라임/실버2

for i in range(2,100001):
    if sosu[i]:
        for j in range(i*2,b+1,i):
            sosu[j] = False
            now = j
            while(now%i == 0):
                now/=i
                nums[j] += 1

for k in range(a,b+1):
    if sosu[nums[k]]:
        ans+=1

print(ans)

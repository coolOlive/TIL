# 유클리드호제법,파싱_백대열/실버5

def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

nums=list(map(int,input().split(':')))

tmp=gcd(min(nums),max(nums))
print(str(nums[0]//tmp)+':'+str(nums[1]//tmp))
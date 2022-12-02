import sys
input=sys.stdin.readline

# 수학,그리디/캠핑/브론즈1
# 우테코 프리코스 2주차 하는중..

i=1
while True:
    l,p,v=map(int,input().split())
    if l==p==v==0:
        break
    tmp=(v//p)*l
    tmp+=min((v%p),l)
    print('Case '+str(i)+': '+str(tmp))
    i+=1
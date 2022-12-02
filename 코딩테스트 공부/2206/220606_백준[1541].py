# 수학,그리디,문자열,파싱_잃어버린 괄호/실버2

arr1=input().split('-')
num=[]

for a in arr1:
    tmp=0
    arr_tmp=a.split('+')
    for b in arr_tmp:
        tmp+=int(b)
    num.append(tmp)

ans=num[0]
for i in range(1,len(num)):
    ans-=int(num[i])

print(ans)
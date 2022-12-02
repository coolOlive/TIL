# 수학,그리디,정렬_30/실버4

num=list(input())
num.sort(reverse=True)
hap=0

if '0' not in num:
    print(-1)
else:
    for n in num:
        hap+=int(n)
    if hap%3!=0:
        print(-1)
    else:
        print(''.join(num))
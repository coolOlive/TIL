# 기본수학1_부녀회장이 될테야/브론즈1

t=int(input())

for _ in range(t):
    k=int(input())
    n=int(input())
    p_num=[i for i in range(1,n+1)]
    for i in range(k):
        for j in range(1,n):
            p_num[j]+=p_num[j-1]
    print(p_num[-1])
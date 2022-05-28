import sys
input=sys.stdin.readline

# 해시_패션왕 신해빈/실버3

test_case=int(input().strip())

for _ in range(test_case):
    dic={}
    n=int(input().strip())
    for i in range(n):
        d_name,d_class=map(str,input().split())
        if not d_class in dic:
            dic[d_class]=1
        else:
            dic[d_class]+=1

    ans=1

    for key in dic.keys():
        ans*=dic[key]+1

    print(ans-1)
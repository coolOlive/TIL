import sys
input=sys.stdin.readline

# 정렬,트리_전화번호 목록/골드4
# 트리..?로 할 수도 있구나..?

t=int(input())

for _ in range(t):
    n=int(input())
    nums=[input().strip() for __ in range(n)]

    nums.sort()
    
    for i in range(n-1):
        tmp=nums[i]
        if tmp == nums[i+1][:len(tmp)]:
            print('NO')
            break
    else:
        print('YES')
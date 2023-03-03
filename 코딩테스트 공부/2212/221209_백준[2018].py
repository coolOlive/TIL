# 투포인터/수들의 합 5/실버5

n = int(input())
start, end = 0, 0
ans, sumNum = 0, 0

while end <= n:
    if sumNum < n:
        end += 1
        sumNum += end
    elif sumNum == n:
        ans +=1
        end +=1
        sumNum += end
    else:
        sumNum -= start
        start +=1

print(ans)
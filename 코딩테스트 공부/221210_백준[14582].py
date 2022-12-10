# 구현/오늘도 졌다/실버5

gemi = list(map(int,input().split()))
startlink = list(map(int,input().split()))

gScore, sScore = 0, 0

for i in range(9):
    gScore += gemi[i]
    if gScore > sScore:
        print('Yes')
        break
    elif i == 8 and gScore <= sScore:
        print('No')
    sScore += startlink[i]


# 수학,비트마스킹_막대기/실버5

x=int(input())
stick=[64]

while sum(stick)>x:
    stick.sort()
    stick[0]//=2
    if sum(stick)<x:
        stick.append(stick[0])
    
print(len(stick))
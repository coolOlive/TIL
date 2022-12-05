import sys
input=sys.stdin.readline

# 구현,수학/약수들의 합/브론즈1

notPerfect = 'is NOT perfect.'

while True:
    num = int(input())
    if num==-1:
        break
    small = []
    for i in range(1,num):
        if num%i==0:
            small.append(i)
    if sum(small)==num:
        print(num,'=', ' + '.join(map(str,small)))
        continue
    print(num,notPerfect)
# 수학,구현,사칙연산_지능형 기차/브론즈3

stay=[0]

for _ in range(4):
    a,b=map(int,input().split())
    stay.append(stay[-1]-a+b)

print(max(stay))
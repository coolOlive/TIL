import sys
input=sys.stdin.readline

 # 정렬,딕셔너리/점수 계산/실버5

dic={int(input()):(i+1) for i in range(8)}

for _ in range(3):
    del dic[min(dic.keys())]

qnum=sorted(dic.values())

print(sum(dic.keys()))
print(' '.join(map(str,qnum)))
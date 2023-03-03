import sys
input=sys.stdin.readline

# 문자열,구현/너의 평점은/실버5

gradeList = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5,
             'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
each = 0
total = 0

for _ in range(20):
    name,score,grade = map(str,input().split())
    score = float(score)
    if grade == 'P':
        continue
    each += score*gradeList[grade]
    total += score

print('{:.6f}'.format(each/total))

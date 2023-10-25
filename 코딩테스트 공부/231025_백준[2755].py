import sys
input=sys.stdin.readline

# 구현/이번학기 평점은 몇점?/브론즈1
# 시험기간이라 한동안 쉬운 문제 풀 예정

dic = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 
      'B-': 2.7, 'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 
      'D0': 1.0, 'D-': 0.7, 'F': 0.0}

t = int(input())
cnt, ans = 0, 0

for _ in range(t):
  name, score, grade = input().split()
  score = int(score)
  ans += score * dic[grade]
  cnt += score

print('%.2f' % (round(ans/cnt + 10**-10, 2)))

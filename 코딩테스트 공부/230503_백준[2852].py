import sys
input=sys.stdin.readline

# 문자열,구현/NBA 농구/실버3

n = int(input())
score = [0,0]
flg = 0

for _ in range(n):
  team,goal = input().split()
  team = int(team)-1
  m,s = map(int,goal.split(':'))
  time = 48*60-(m*60 + s)

  if flg==0:
    score[team] += time
      
  if team:
    flg += 1
  else:
    flg -= 1
  
  if flg==0 and score[team^1] > 0:
    score[team^1] -= time

print('{:0>2}:{:0>2}'.format(score[0]//60, score[0]%60))
print('{:0>2}:{:0>2}'.format(score[1]//60, score[1]%60))

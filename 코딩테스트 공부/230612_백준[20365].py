import sys
input = sys.stdin.readline

# 문자열,그리디/블로그2/실버3

n = int(input())
s = input().strip()

colors = {'B':0,'R':0}
colors[s[0]] +=1

for i in range(1, n):
  if s[i] != s[i-1]:
    colors[s[i]] += 1

print(min(colors['B'], colors['R']) + 1)

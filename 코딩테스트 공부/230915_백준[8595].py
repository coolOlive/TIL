import sys
input=sys.stdin.readline

# 문자열/히든 넘버/브론즈1

n = int(input())
word = input().strip()
nums = ['0','1','2','3','4','5','6','7','8','9']
hidden = ''
ans = []

for w in word:
  if w in nums:
    hidden += w
  elif len(hidden)<7 and len(hidden)!=0:
    ans.append(int(hidden))
    hidden = ''

if len(hidden)<7 and len(hidden) != 0:
  ans.append(int(hidden))

print(sum(ans))

import sys
input=sys.stdin.readline

# 문자열,구현,그리디/팰린드롬 만들기/실버3

name = list(input().strip())
dic = dict()
ans = ''

for n in name:
  if n in dic:
    dic[n] += 1
  else:
    dic[n] = 1

s_name = sorted(list(set(name)))

for n in s_name:
  for i in range(dic[n]//2):
    ans += n

if len(name)%2==0:
  ans += ans[-1::-1]
else:
  tmp = ''
  for a,b in dic.items():
    if b%2!=0:
        tmp = a
  ans = ans + tmp + ans[-1::-1]

if len(ans) != len(name):
  print("I'm Sorry Hansoo")
else:
  print(ans)

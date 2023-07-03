import sys
input = sys.stdin.readline

# 그리디,문자열/부분 문자열/실버5

while 1:
  try:
    s,t = map(str,input().split())
    idx = 0
    ans = 'No'

    for i in range(len(t)):
      if s[idx] == t[i]:
        idx += 1
          
      if len(s)==idx:
        ans = 'Yes'
        break
    print(ans)

  except:
    break

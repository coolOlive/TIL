import sys
input = sys.stdin.readline

# 자료구조,브루트포스/행운의 수/실버4

T = int(input())

for tc in range(T):
  abc, lstabc = [], []
  ans = set()

  for _ in range(3):
    abc.append(int(input()))
    lstabc.append(list(map(int,input().split())))

  for a in lstabc[0]:
    for b in lstabc[1]:
      for c in lstabc[2]:
        tmp = str(a+b+c)
        flg = True
        for t in tmp:
          if t=='5' or t=='8':
            continue
          else:
            flg = False
            break
        if flg:
          ans.add(tmp)
  print(len(ans))

  
# 브루트포스,백트래킹/에너지 모으기/실버1

n = int(input())
w = list(map(int,input().split()))
ans = 0

def energe(e):
  global ans
  tmp = len(w)

  if tmp == 2:
    ans = max(ans, e)
    return

  for i in range(1,tmp-1):
    getE = w[i-1]*w[i+1]
    removeW = w.pop(i)
    energe(e+getE)
    w.insert(i,removeW)

energe(0)
print(ans)
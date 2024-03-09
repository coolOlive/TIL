# 그리디,정렬/귤 고르기/L2

def solution(k, tangerine):
  ans, cnt = 0, 0
  tDic = dict()
  for t in tangerine:
    tDic[t] = tDic.get(t,0) + 1
  
  sortt = sorted(tDic.values(), reverse = True)
  
  for t in sortt:
    cnt += t
    ans += 1
    if cnt>=k:
      break

  return ans

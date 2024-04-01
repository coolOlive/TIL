# 정렬/H-Index/L2

def solution(citations):
  citations.sort(reverse=True)
  
  for i in range(len(citations)):
    if(citations[i] < i+1):
      return i

  return len(citations)

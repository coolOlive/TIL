# 해시/베스트앨범/L3

def solution(genres, plays):
  answer = []
  gCnt = dict()
  genre = dict()
  
  for i in range(len(genres)):
    gCnt[genres[i]] = gCnt.get(genres[i],0)+plays[i]
    genre[genres[i]] = genre.get(genres[i],[])+[(i,plays[i])]
  
  gCnt = sorted(gCnt.items(),key = lambda x:x[1],reverse = True)
  
  for g,cnt in gCnt:
    tmp = sorted(genre[g], key = lambda x : (-x[1],x[0]))
    ansCount = 0
    
    for t in tmp:
      if ansCount>1:
        break
      answer.append(t[0])
      ansCount += 1
          
  return answer
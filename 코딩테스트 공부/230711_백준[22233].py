import sys
input=sys.stdin.readline

# 자료구조/가희와 키워드/실버2

n, m = map(int, input().split())
ans = n
word = dict()

for _ in range(n) :
  word[input().strip()] = 1
        
for _ in range(m) :
  tmp = sorted(input().strip().split(','))
      
  for t in tmp :
    if t in word.keys():
      if word[t] == 1:
        word[t] -= 1
        ans -= 1
            
  print(ans)

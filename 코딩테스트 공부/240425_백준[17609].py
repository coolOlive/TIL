import sys
input = sys.stdin.readline

# 투포인터,문자열/회문/골드5

n = int(input())

def check(word):
  l,r = 0,len(word)-1

  while l<r:
    if word[l]==word[r]:
      l += 1
      r -= 1
      continue
    if word[l] == word[r-1]:
      tmp = word[l:r]
      if tmp[:]==tmp[::-1]:
        return 1
    if word[l+1] == word[r]:
      tmp = word[l+1:r+1]
      if tmp[:] == tmp[::-1]:
        return 1
    return 2
  return 0

for _ in range(n):
  word = input().strip()
  print(check(word))

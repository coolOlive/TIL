import sys
input=sys.stdin.readline

# 구현,문자열/팬그램/실버5

n = int(input())

for i in range(n):
  words = input().strip()
  words = words.lower()
  tmp=[0]*26
  
  for s in words:
    if s.isalpha():
      tmp[ord(s)-97]+=1

  mini = min(tmp)
  
  if mini>=3:
    print("Case {}: Triple pangram!!!".format(i+1))
    continue
  if mini>=2:
    print("Case {}: Double pangram!!".format(i+1))
    continue
  if mini>=1:
    print("Case {}: Pangram!".format(i+1))
    continue
  print("Case {}: Not a pangram".format(i+1))

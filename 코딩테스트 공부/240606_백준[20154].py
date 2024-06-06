import sys
input=sys.stdin.readline

# 수학,문자열/이 구역의 승자는 누구야?!/브론즈1

alpha = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
s = input().strip()
word = []

for a in s:
  i = ord(a)-ord('A')
  word.append(alpha[i])

if sum(word)%10%2:
  print("I'm a winner!")
else:
  print("You're the winner?")

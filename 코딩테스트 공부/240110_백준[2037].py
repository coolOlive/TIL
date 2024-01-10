import sys
input=sys.stdin.readline

# 구현/문자메시지/브론즈1

p, w = map(int, input().split())
words = input()
ans = 0
before = ''
phone = [[], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]


for i in range(len(words)):
  if words[i] == ' ':
    ans += p
    before = ''
  for j in range(9):
    for k in range(len(phone[j])):
      if words[i] == phone[j][k]:
        if j==before:
          ans += w
        ans += p*(1+k)
        before = j

print(ans)

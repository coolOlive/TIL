import sys
input=sys.stdin.readline

# 수학,구현/중복된 숫자/실버5
# 계속 시간초과, 메모리초과나서 어려웠다.
# 실버5가 왜 이렇지?

n = int(input())
nums = input().rstrip()
ok = sum(range(1, int(n)))

toatal = 0
tmp = ''

for num in nums:
  if num.isdigit():
    tmp += num
  else:
    toatal += int(tmp)
    tmp = ''

toatal += int(tmp)

print(toatal - ok)

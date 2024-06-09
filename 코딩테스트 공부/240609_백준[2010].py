import sys
input = sys.stdin.readline

# 수학/플러그/브론즈3

num = int(input())
hap = 1

for i in range(num):
  hap += int(input())

print(hap-num)

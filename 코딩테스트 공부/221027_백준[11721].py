import sys
# 문자열/열 개씩 끊어 출력하기/브론즈3
# 당분간 쉬운거 할듯

input=sys.stdin.readline
s=input().strip()

for i in range(0,len(s),10):
    print(s[i:i+10])
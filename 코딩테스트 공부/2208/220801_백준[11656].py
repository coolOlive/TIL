import sys
input=sys.stdin.readline

# 문자열,정렬_접미사 배열/실버4


s=input().strip()

s_arr=[s[i:] for i in range(len(s))]
s_arr.sort()

print('\n'.join(s_arr))
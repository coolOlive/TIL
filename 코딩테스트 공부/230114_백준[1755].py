import sys
input=sys.stdin.readline

# 정렬,해시,문자열/숫자놀이/실버4

m,n = map(int,input().split())

alpha = ['zero','one','two','three','four','five',
         'six','seven','eight','nine']
ans = dict()
number = []

for i in range(m,n+1):
    a,b = i//10, i%10
    tmp = ''
    if a != 0:
        tmp += (alpha[a] + ' ')
    tmp += alpha[b]
    ans[tmp] = i
    number.append(tmp)

number.sort()

for j in range(n-m+1):
    if j%10 == 0 and j!= 0:
        print()
    print(ans[number[j]],end = ' ')

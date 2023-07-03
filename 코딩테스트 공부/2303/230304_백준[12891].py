import sys
input=sys.stdin.readline

# 슬라이딩윈도우/DNA 비밀번호/실버2

s,p = map(int,input().split())
dna = input().strip()
a,c,g,t = map(int,input().split())
tmp = {'A':0, 'C':0, 'G':0, 'T':0}
ans = 0

password = dna[:p]
for pa in password:
    tmp[pa] += 1

if tmp['A'] >= a and tmp['C'] >= c and tmp['G'] >= g and tmp['T'] >= t:
    ans += 1
    
left,right = 0,p

def check(tmp):
    if tmp['A'] >= a and tmp['C'] >= c and tmp['G'] >= g and tmp['T'] >= t:
        return 1
    return 0
    
for i in range(s-p):
    tmp[dna[left+i]] -= 1
    tmp[dna[right+i]] += 1
    if tmp['A'] >= a and tmp['C'] >= c and tmp['G'] >= g and tmp['T'] >= t:
        ans += 1
    
print(ans)

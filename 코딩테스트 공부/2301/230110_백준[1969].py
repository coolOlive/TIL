from itertools import combinations
import sys
input=sys.stdin.readline

# 브루트포스,문자열,구현/DNA/실버5

n, m = map(int,input().split())
dna = [input().strip() for _ in range(n)]
nucleo_name = ['A','C','G','T']
ans = ''
hamming = 0

for i in range(m):
    nucleo = [0,0,0,0]
    for j in range(n):
        if dna[j][i] == 'A':
            nucleo[0] += 1
        elif dna[j][i] == 'C':
            nucleo[1] += 1
        elif dna[j][i] == 'G':
            nucleo[2] += 1
        elif dna[j][i] == 'T':
            nucleo[3] += 1
    ans += nucleo_name[nucleo.index(max(nucleo))]
    hamming += n - max(nucleo)

print(ans)
print(hamming)

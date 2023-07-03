import sys
input = sys.stdin.readline

# 구현/DNA 해독/브론즈1

n = int(input())
dna = list(input().rstrip())
name = {"AG":"C", "AC":"A", "AT":"G", "GC":"T", "GT":"A", "CT":"G", "GA":"C", "CA":"A", "TA":"G", "CG":"T", "TG":"A","TC":"G"}

a,b = "", dna.pop()
for _ in range(n-1):
  a = dna.pop()
  if a == b:
    continue
  b = name[a+b]
    
print(b)

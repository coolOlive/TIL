import re
import sys
input=sys.stdin.readline

# 정규표현식/염색체/실버3

pattern = re.compile('[A-F]?A+F+C+[A-F]?$')

for _ in range(int(input())):
  dna = input().strip()
  if pattern.match(dna):
    print('Infected!')
  else:
    print('Good')

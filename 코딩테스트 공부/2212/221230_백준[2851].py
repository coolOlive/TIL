import sys
input=sys.stdin.readline

# 구현/슈퍼 마리오/브론즈1

mario = [int(input()) for _ in range(10)]
score = 0

for a in mario:
    score += a
    if score >= 100:
        if score - 100 > 100 - (score - a):
            score -= a
        break
    
print(score)

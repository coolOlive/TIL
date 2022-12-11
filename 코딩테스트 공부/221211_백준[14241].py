# 수학/슬라임 합치기/실버3

n = int(input())
slime = list(map(int,input().split()))
slime.sort(reverse=True)
score = 0

for i in range(n-1):
    score += slime[i] * slime[i+1]
    slime[i+1] = slime[i] + slime[i+1]

print(score)
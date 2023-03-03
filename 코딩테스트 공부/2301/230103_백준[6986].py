import sys
input = sys.stdin.readline

# 구현,정렬/절사평균/실버3

n, k = map(int, input().split())
score = [float(input()) for _ in range(n)]
score.sort()

cutScore = score[k:n-k]
ans1 = ans2 = sum(cutScore)
ans1 /= (n-2*k)
ans2 += (score[k]*k) + (score[n-k-1]*k)
ans2 /= n

print('%.2f'%(ans1+0.00000001))
print('%.2f'%(ans2+0.00000001))

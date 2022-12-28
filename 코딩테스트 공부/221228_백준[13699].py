# dp/점화식/실버4

n = int(input())
t = [1,1,2,5] + [0 for _ in range(32)]

if n > 3:
    for i in range(4,n+1):
        for j in range(i):
            t[i] += t[j] * t[i-j-1]

print(t[n])
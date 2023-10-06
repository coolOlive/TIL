import sys
input=sys.stdin.readline

# 자료구조/추월/실버1

n = int(input())
ans = 0
enter, out = {}, []

for i in range(n):
	enter[input().strip()] = i
	
for _ in range(n):
	out.append(input().strip())

for i in range(n-1):
  for j in range(i+1, n):
    if enter[out[i]] > enter[out[j]]:
      ans += 1
      break
print(ans)

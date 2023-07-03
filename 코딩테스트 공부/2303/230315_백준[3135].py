# 그리디,수학/라디오/실버5

a,b = map(int, input().split())
n = int(input())

radio = [abs(int(input())-b) for _ in range(n)]

print(min(abs(a-b), min(radio)+1))

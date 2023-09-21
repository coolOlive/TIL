# 문자열,수학/2진수 뒤집기/브론즈1

n = int(input())
binum = bin(n)
num = str(binum[2:])[::-1]
ans = int(num,2)

print(ans)

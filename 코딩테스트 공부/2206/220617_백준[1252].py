# 수학,구현,사칙연산_이진수 덧셈/브론즈2

a,b=map(int,input().split())

a=int(str(a),2)
b=int(str(b),2)

print(bin(a+b)[2:])
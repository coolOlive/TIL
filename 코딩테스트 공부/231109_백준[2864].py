# 문자열/5와 6의 차이/브론즈2

a,b = input().split()

large = int(a.replace('6', '5')) + int(b.replace('6', '5'))
small = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(large, small)
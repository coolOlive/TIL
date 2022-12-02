# 문자열,구현/ROT13/브론즈1
# 우테코 문풀하는 중이라 당분간 쉬운거 할듯

s=input()
ans=''

for c in s:
    tmp=ord(c)+13
    if 'a'<=c<='z':
        ans += chr(tmp if chr(tmp) <= 'z' else ord(c)-13)
    elif 'A'<=c<='Z':
        ans += chr(tmp if chr(tmp) <= 'Z' else ord(c)-13)
    else:
        ans+=c

print(ans)
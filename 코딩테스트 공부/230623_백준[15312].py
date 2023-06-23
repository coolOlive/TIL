# 다이나믹,문자열/이름 궁합/실버5

name1 = input()
name2 = input()
alpha = {'A':3,'B':2,'C':1,'D':2,'E':3,'F':3,
          'G':2, 'H':3, 'I':3, 'J':2, 'K':2, 'L':1, 'M':2, 'N':2, 'O':1,
         'P':2, 'Q':2, 'R':2, 'S':1, 'T':2, 'U':1, 'V':1, 'W':1, 'X':2, 'Y':2, 'Z':1}
name = []

for i in range(len(name1)):
  name.append(alpha[name1[i]])
  name.append(alpha[name2[i]])

while len(name) != 2:
  tmp = []
  for i in range(1, len(name)):
    tmp.append((name[i] + name[i-1]) % 10)
  name = tmp

print(str(name[0])+str(name[1]))

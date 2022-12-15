import sys
input=sys.stdin.readline

# 스택/키로거/실버2

t = int(input())

for _ in range(t):
    right,left = [], []
    password = input().strip()
    for word in password:
        if word == '<':
            if left:
                right.append(left.pop())
        elif word == '>':
            if right:
                left.append(right.pop())
        elif word == '-':
            if left:
                left.pop()
        else:
            left.append(word)
    left.extend(reversed(right))
    print(''.join(left))
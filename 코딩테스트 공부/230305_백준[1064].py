# 피타고라스 정리/평행사변형/실버5

ax, ay, bx, by, cx, cy = map(int, input().split())

if ((ax-bx)*(ay-cy)==(ay-by)*(ax-cx)):
    print(-1.0)
else:
    ab_len = ((ax-bx)**2 + (ay-by)**2)**0.5
    ac_len = ((ax-cx)**2 + (ay-cy)**2)**0.5
    bc_len = ((bx-cx)**2 + (by-cy)**2)**0.5

    length = [ab_len+ac_len, ab_len+bc_len, ac_len+bc_len]
    print(2*(max(length) - min(length)))

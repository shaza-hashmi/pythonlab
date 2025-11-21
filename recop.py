class R:
    def __init__(s,l,w): s.l=l;s.w=w
    def a(s): return s.l*s.w
    def __lt__(s,o): return s.a()<o.a()
r1=R(*map(int,input("Rect1: ").split()))
r2=R(*map(int,input("Rect2: ").split()))
print(r1<r2)


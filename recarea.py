class R:
    def __init__(s,l,b): s.l=l;s.b=b
    def a(s): return s.l*s.b
r1=R(*map(int,input("Rect1 l b: ").split()))
r2=R(*map(int,input("Rect2 l b: ").split()))
print("r1<r2:", r1.a()<r2.a())


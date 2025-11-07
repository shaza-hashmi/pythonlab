class Rect:
    def __init__(s,l,w): s.l=l; s.w=w
    def area(s): return s.l*s.w
    def __lt__(s,o): return s.area()<o.area()
r1=Rect(*map(int,input("Rect1 l w: ").split()))
r2=Rect(*map(int,input("Rect2 l w: ").split()))
print("r1<r2:",r1<r2)


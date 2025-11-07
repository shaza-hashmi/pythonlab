class Time:
    def __init__(s,h,m,sec): s.h=h; s.m=m; s.s=sec
    def __add__(s,o):
        sec=s.s+o.s; m=s.m+o.m+sec//60; h=s.h+o.h+m//60
        return Time(h%24,m%60,sec%60)
    def show(s): print(f"{s.h}:{s.m}:{s.s}")

h1,m1,s1=map(int,input("Time1 h m s: ").split())
h2,m2,s2=map(int,input("Time2 h m s: ").split())
t1,t2=Time(h1,m1,s1),Time(h2,m2,s2)
(t1+t2).show()


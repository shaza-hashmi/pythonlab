class T:
    def __init__(s,h,m,se): s.h=h;s.m=m;s.s=se
    def __add__(s,o):
        s1=s.s+o.s;m1=s.m+o.m+s1//60;h1=s.h+o.h+m1//60
        return T(h1%24,m1%60,s1%60)
t1=T(*map(int,input("Time1 h m s: ").split()))
t2=T(*map(int,input("Time2 h m s: ").split()))
r=t1+t2
print(r.h,r.m,r.s)


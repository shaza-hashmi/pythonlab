class Pub:
    def __init__(s,n): s.n=n
class Book(Pub):
    def __init__(s,n,t,a): super().__init__(n); s.t=t; s.a=a
class Py(Book):
    def __init__(s,n,t,a,p,pg): super().__init__(n,t,a); s.p=p; s.pg=pg
    def show(s): print(s.n,s.t,s.a,s.p,s.pg)

n=input("Publisher: ")
t=input("Title: ")
a=input("Author: ")
p=int(input("Price: "))
pg=int(input("Pages: "))
Py(n,t,a,p,pg).show()


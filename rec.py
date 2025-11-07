class Rectangle:
    def __init__(self,l,b):
        self.l=l; self.b=b
    def area(self):
        return self.l*self.b

l1,b1=map(int,input("Rect1 l,b: ").split())
l2,b2=map(int,input("Rect2 l,b: ").split())
r1,r2=Rectangle(l1,b1),Rectangle(l2,b2)
print("Area1:",r1.area(),"Area2:",r2.area())
print("Larger:", "Rect1" if r1.area()>r2.area() else "Rect2")


from graphics import rectangle, circle
from graphics.ThreeDgraphics import cuboid, sphere


print("\n--- Rectangle ---")
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
print("Area =", rectangle.area(l, b))
print("Perimeter =", rectangle.perimeter(l, b))


print("\n--- Circle ---")
r = float(input("Enter radius: "))
print("Area =", circle.area(r))
print("Perimeter =", circle.perimeter(r))


print("\n--- Cuboid ---")
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))
print("Surface Area =", cuboid.surface_area(l, b, h))
print("Volume =", cuboid.volume(l, b, h))

print("\n--- Sphere ---")
r = float(input("Enter radius: "))
print("Surface Area =", sphere.surface_area(r))
print("Volume =", sphere.volume(r))


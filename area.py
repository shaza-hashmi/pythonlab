a = float(input("side: "))
l, b = map(float, input("length breadth: ").split())
ba, h = map(float, input("base height: ").split())

print(
    "square = ", (lambda a: a * a)(a),
    "rectangle = ", (lambda l, b: l * b)(l, b),
    "triangle = ", (lambda b, h: 0.5 * b * h)(ba, h)
)



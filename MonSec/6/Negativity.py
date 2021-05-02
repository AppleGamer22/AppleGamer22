from tinyec.ec import Curve, Point, SubGroup


P = (8045, 6936)
mod = 9739
a = 497
b = 1768
field = SubGroup(p = mod, g = P, n = mod + 1, h = 1)
curve = Curve(a = a, b = b, field = field, name = "Y^2 = X^3 + 497 X + 1768 mod 9739")
point1 = Point(curve, P[0], P[1])
point2 = Point(curve, P[0], -P[1] % 9739)
coordinate = (point2.x, point2.y)
print(coordinate)
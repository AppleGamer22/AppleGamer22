from tinyec.ec import Curve, Point, SubGroup


P = (5053, 3507)
mod = 9739
a = 497
b = 1768
field = SubGroup(p = mod, g = P, n = mod + 1, h = 1)
curve = Curve(a = a, b = b, field = field, name = "Y^2 = X^3 + 497 X + 1768 mod 9739")
point_p = Point(curve, P[0], P[1])
point_q = point_p * 107
coordinates = (point_q.x, point_q.y)
print(coordinates)
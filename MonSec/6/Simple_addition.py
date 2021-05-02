from tinyec.ec import Curve, Point, SubGroup


P = (8148, 2505)
Q = (5685, 2615)
mod = 9739
a = 497
b = 1768
field = SubGroup(p = mod, g = P, n = mod + 1, h = 1)
curve = Curve(a = a, b = b, field = field, name = "Y^2 = X^3 + 497 X + 1768 mod 9739")
point_p = Point(curve, P[0], P[1])
point_q = Point(curve, Q[0], Q[1])
point_r = point_p + point_q
coordinates = (point_r.x, point_r.y)
print(coordinates)
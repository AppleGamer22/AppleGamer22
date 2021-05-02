from tinyec.ec import Curve, Point, SubGroup


G = (5083, 5692)
Q = (8568, 4147)
mod = 9739
a = 497
b = 1768
field = SubGroup(p = mod, g = G, n =mod + 1, h = 1)
curve = Curve(a = a, b = b, field = field, name = "Y^2 = X^3 + 497 X + 1768 mod 9739")
point_g = Point(curve, G[0], G[1])
point_q = Point(curve, Q[0], Q[1])

for i in range(1000):
	if point_g * i == point_q:
		print(i)
		break
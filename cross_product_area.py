import math

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def cross(a, b):
    return [
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]
    ]

def norm(v):
    return math.sqrt(dot(v, v))

u = [1.0, 2.0, 2.0]
v = [2.0, 1.0, 3.0]

c = cross(u, v)

print("u =", u)
print("v =", v)
print("u x v =", c)
print("(u x v) · u =", dot(c, u))
print("(u x v) · v =", dot(c, v))

area_parallelogram = norm(c)
area_triangle = area_parallelogram / 2

print("area (parallelogram) =", area_parallelogram)
print("area (triangle) =", area_triangle)

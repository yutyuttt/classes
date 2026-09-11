import math

for k in range(11):
    alpha = k * math.pi/5

    a = alpha
    b = math.sin(alpha)
    c = math.cos(alpha)

    print(a, b, c)
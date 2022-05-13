import sympy as sp

x = sp.symbols('x')
f = x ** 2 - 5 * x + 2
f_prime = f.diff(x)
f = sp.lambdify(x, f)
f_prime = sp.lambdify(x, f_prime)
_range = [0, 5]
eps = 0.0001
sectionSize = 0.1
numOfSections = int((_range[1] - _range[0]) / sectionSize) + 1


def Newton_Raphson(f, _range, eps):
    x1 = (_range[0] + _range[1]) / 2
    for i in range(numOfSections):
        x2 = x1 - (f(x1) / f_prime(x1))
        if abs(x2 - x1) < eps:
            return [x2, i + 1]
        x1 = x2
    return False

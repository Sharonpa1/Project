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


def secant_method(f, _range, eps):
    x1 = _range[0]
    x2 = _range[1]
    for i in range(numOfSections):
        x3 = (x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))
        if abs(x2 - x1) < eps:
            return [x3, i + 1]
        x1 = x2
        x2 = x3
    return False

from math import *

import sympy as sp


def bisection_method(f, _range, eps):
    a = _range[0]
    b = _range[1]
    c = (a + b) / 2
    prev_c = c - 1
    min_iterations = 10
    index = 1
    while prev_c != c or min_iterations > 0:
        prev_c = c
        c = (a + b) / 2
        if f(a) * f(c) == 0:
            pass
        elif f(a) * f(c) > 0:
            a = c
        else:
            b = c

        min_iterations = min_iterations - 1
        index = index + 1

    return [c, index]


def Newton_Raphson(f, _range, eps):
    x1 = (_range[0] + _range[1]) / 2
    for i in range(numOfSections):
        x2 = x1 - (f(x1) / f_prime(x1))
        if abs(x2 - x1) < eps:
            return [x2, i + 1]
        x1 = x2
    return False


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


x = sp.symbols('x')
f = (sp.sin(x ** 4 + 5 * x - 6)) / (2 * e ** (-2 * x + 5))
f_prime = f.diff(x)
f = sp.lambdify(x, f)
f_prime = sp.lambdify(x, f_prime)
_range = [-1.5, 1.5]
eps = 0.0001
sectionSize = 0.1
numOfSections = int((_range[1] - _range[0]) / sectionSize) + 1
roots_dict = {}


choice = input("Choose an option:\n1 - bisection method\n2 - Newton Raphson method\n3 - secant method\n>>> ")
if choice != '1' and choice != '2' and choice != '3':
    print("Wrong input. The program will close.")
    exit()


_x = _range[0]
for i in range(numOfSections):
    f_x1 = f(_x)
    f_x2 = f(_x + sectionSize)
    if f_x1 * f_x2 < 0:
        if choice == '1':
            root = bisection_method(f, [_x, _x + sectionSize], eps)
        if choice == '2':
            root = Newton_Raphson(f, [_x, _x + sectionSize], eps)
        if choice == '3':
            root = secant_method(f, [_x, _x + sectionSize], eps)
        if root:
            roots_dict[root[0]] = root[1]
    _x += sectionSize


if choice == '1':
    _x = _range[0]
    for i in range(numOfSections):
        f_x1 = f_prime(_x)
        f_x2 = f_prime(_x + sectionSize)
        if f_x1 * f_x2 <= 0:
            if f_x1 * f_x2 == 0:
                root = bisection_method(f_prime, [_x, _x + 2 * sectionSize], eps)
            else:
                root = bisection_method(f_prime, [_x, _x + sectionSize], eps)
            if f(root[0]) == 0:
                roots_dict[root[0]] = root[1]
        _x += sectionSize
        _x = float("{0:.5f}".format(_x))


if len(roots_dict) == 0:
    print("No roots founded.")

for item in roots_dict:
    print("Root:", item, ", founded after:", roots_dict[item], "iterations.")
    # print("Root:", float("{0:.6f}".format(item)), ", founded after:", roots_dict[item], "iterations.")

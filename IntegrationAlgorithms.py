import math
from math import *


def function(x):
    function = sin(x)
    return (function)


upper = math.pi
lower = 0
intervals = 4
h = (upper - lower) / intervals
z = intervals / 2
ans = 0


def trapeziumrule():
    rule = 0
    x = lower
    rule += function(x)
    x = upper
    rule += function(x)
    for i in range(1, intervals):
        x = lower + h*i
        rule += 2 * (function(x))
    ans = (h/2) * rule
    return (ans)


def simpsonsrule():
    rule = 0
    x = lower + h
    for i in range(1, int(z+1)):
        rule += 4*function(x)
        x += 2*h

    x = lower + 2*h
    for i in range(1, int(z)):
        rule += 2 * function(x)
        x += 2*h
    ans = (h/3)*(function(lower) + function(upper)+rule)
    return (ans)


print(trapeziumrule())
print(simpsonsrule())

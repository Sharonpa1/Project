def gauss(m):
    # eliminate columns
    for col in range(len(m[0])):
        for row in range(col+1, len(m)):
            r = [(rowValue * (-(m[row][col] / m[col][col]))) for rowValue in m[col]]
            m[row] = [sum(pair) for pair in zip(m[row], r)]
    # now backsolve by substitution
    ans = []
    m.reverse() # makes it easier to backsolve
    for sol in range(len(m)):
        if sol == 0:
            ans.append(m[sol][-1] / m[sol][-2])
        else:
            inner = 0
            # substitute in all known coefficients
            for x in range(sol):
                inner += (ans[x]*m[sol][-2-x])
            # the equation is now reduced to ax + b = c form
            # solve with (c - b) / a
            ans.append((m[sol][-1]-inner)/m[sol][-sol-2])
    ans.reverse()
    return ans


def linearInterpolation(tbl, x):
    for i in range(len(tbl)):
        x1 = tbl[i][0]
        y1 = tbl[i][1]
        x2 = tbl[i + 1][0]
        y2 = tbl[i + 1][1]

        if x1 <= x <= x2:
            return (((y1 - y2) / (x1 - x2)) * x) + ((y2 * x1 - y1 * x2) / (x1 - x2))


def polynomialInterpolation(tbl, x):
    m = []
    for i in range(len(tbl)):
        row = [1, tbl[i][0], (tbl[i][0])**2, tbl[i][1]]
        m.append(row)

    a = gauss(m)
    ans = 0
    for i in range(len(a)):
        ans += a[i] * x**i

    return ans


def lagrangeInterpolation(tbl, x):
    p = 0
    for i in range(len(tbl)):
        l = 1
        for j in range(len(tbl)):
            if i == j:
                continue
            l *= ((x - tbl[j][0]) / (tbl[i][0] - tbl[j][0]))
        p += l * tbl[i][1]
    return p


def nevilleInterpolation(tbl, x):
    size = len(tbl)
    iteration_num = 1
    tmp_list = []
    for i in range(len(tbl)):
        tmp_list.append(tbl[i][1])
    while size > 1:
        p_list = tmp_list
        tmp_list = []
        for i in range(len(tbl) - iteration_num):
            x1 = tbl[i][0]
            p1 = p_list[i]
            x2 = tbl[i + iteration_num][0]
            p2 = p_list[i + 1]
            p = ((x - x1) * p2 - (x - x2) * p1) / (x2 - x1)
            tmp_list.append(p)
        iteration_num += 1
        size -= 1
    return tmp_list[0]


def cubic_splinesInterpolation(tbl, x):
    pass


# tbl = ((0, 0), (1, 0.8415), (2, 0.9093), (3, 0.1411), # TODO לבדוק למה לא עובד עם הדוגמא הזאת
#        (4, -0.7568), (5, -0.9589), (6, -0.2794))
# x = 2.5

# tbl = ((1, 0.8415), (2, 0.9093), (3, 0.1411))
# x = 2.5

# tbl = ((1, 1), (2, 0), (4, 1.5))
# x = 3

tbl = ((1, 0), (1.2, 0.112463), (1.3, 0.167996), (1.4, 0.222709))
x = 1.28

if x < tbl[0][0] or x > tbl[len(tbl) - 1][0]:
    print("x is not in range")
    exit()

# print("Linear Interpolation:", linearInterpolation(tbl, x))
# # print(gauss([[1, 1, 1, 0.8415], [1, 2, 4, 0.9093], [1, 3, 9, 0.1411]]))
# print("Polynomial Interpolation:", polynomialInterpolation(tbl, x))
print("Lagrange Interpolation:", lagrangeInterpolation(tbl, x))
print("Neville Interpolation:", nevilleInterpolation(tbl, x))
print("Cubic Splines Interpolation:", cubic_splinesInterpolation(tbl, x))

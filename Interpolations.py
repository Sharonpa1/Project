def GaussSeidel(matrixA, vectorB):
    num_of_iterations = 1000000
    # if not check(matrixA):
    #     num_of_iterations = 100
    e = 1
    x0 = 0
    y0 = 0
    z0 = 0
    index = 1
    while e >= eps and num_of_iterations > 0:
        x1 = (vectorB[0] - matrixA[0][1] * y0 - matrixA[0][2] * z0) / matrixA[0][0]
        y1 = (vectorB[1] - matrixA[1][0] * x1 - matrixA[1][2] * z0) / matrixA[1][1]
        z1 = (vectorB[2] - matrixA[2][0] * x1 - matrixA[2][1] * y1) / matrixA[2][2]

        print(index, '%0.6f\t%0.6f\t%0.6f\t' % (x1, y1, z1))
        e = abs(x1 - x0)
        x0 = x1
        y0 = y1
        z0 = z1

        index = index + 1
        num_of_iterations = num_of_iterations - 1

    return [x1, y1, z1]
    # print('\nSolution: x = %0.6f, y = %0.6f and z = %0.6f\n' % (x1, y1, z1))


eps = 0.00001


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
    sol = []
    for i in range(len(tbl)):
        row = [1, tbl[i][0], (tbl[i][0])**2, tbl[i][1]]
        m.append(row)
    for i in range(len(tbl)):
        sol.append(tbl[i][1])

    a = GaussSeidel(m, sol)
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
    h_list = []
    l_list = [1]
    mue_list = [0]
    d_list = [0]
    for i in range(len(tbl) - 1):
        h_list.append(tbl[i + 1][0] - tbl[i][0])
    for i in range(1, len(tbl) - 1):
        tmp = h_list[i] / (h_list[i - 1] + h_list[i])
        l_list.append(tmp)
        mue_list.append(1 - tmp)
        d_list.append((6 / (h_list[i - 1] + h_list[i])) *
                      (((tbl[i + 1][1] - tbl[i][1]) / h_list[i]) - ((tbl[i][1] - tbl[i - 1][1]) / h_list[i - 1])))

    h_list.append(1)
    l_list.append(1)
    mue_list.append(0)
    d_list.append(0)

    matrix = []
    row = []
    for i in range(len(tbl) + 1):
        row.append(0)
    for i in range(len(tbl)):
        matrix.append(list(row))
    for i in range(len(tbl)):
        matrix[i][i] = 2

        if i != 0:
            matrix[i][i - 1] = mue_list[i]
        if i != len(tbl) - 1:
            matrix[i][i + 1] = l_list[i]

    m_list = GaussSeidel(matrix, d_list)

    for i in range(len(tbl)):
        x1 = tbl[i][0]
        y1 = tbl[i][1]
        m1 = m_list[i]
        h1 = h_list[i]
        x2 = tbl[i + 1][0]
        y2 = tbl[i + 1][1]
        m2 = m_list[i + 1]
        h2 = h_list[i + 1]
        print(x1,x2,m1,m2,h1,h2, y1, y2)
        if x1 <= x <= x2:
            return (((x2 - x) ** 3 * m1) + ((x - x1) ** 3 * m2)) / (6 * h1) + \
                   ((((x2 - x) * y1) + ((x - x1) * y2)) / h1) - \
                   (((((x2 - x) * m1) + ((x - x1) * m2)) / 6) * h1)


tbl = ((5.5, 3.14), (6.8, 4.35), (7.2, 2.74), (8.3, 5.7))
x = 7

if x < tbl[0][0] or x > tbl[len(tbl) - 1][0]:
    print("x is not in range")
    exit()

print("Linear Interpolation:", linearInterpolation(tbl, x))
print("Polynomial Interpolation:", polynomialInterpolation(tbl, x))
print("Lagrange Interpolation:", lagrangeInterpolation(tbl, x))
print("Neville Interpolation:", nevilleInterpolation(tbl, x))
print("Cubic Splines Interpolation:", cubic_splinesInterpolation(tbl, x))

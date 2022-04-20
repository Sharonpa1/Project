def Mul_Matrix(A, B):
    # צריך לשנות לפי הגודל המתאים
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


def domination(A):
    for i in range(len(A)):
        sum = 0
        for j in range(len(A[i])):
            if i != j:
                sum = sum + abs(A[i][j])
        if abs(A[i][i]) < sum:
            return False
    return True


def OrderPivot(A, col):
    matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    max = abs(A[col][col])
    row_index = col
    for i in range(len(A)):
        if i >= col:
            if abs(A[i][col]) > max:
                max = A[i][col]
                row_index = i

    tmp = matrix[row_index]
    matrix[row_index] = matrix[col]
    matrix[col] = tmp
    return matrix


def pivoting(A):
    for i in range(len(A)):
        for j in range(len(A)):
            E = OrderPivot(A, j)
            A = Mul_Matrix(E, A)
    return A


def check(A):
    if domination(A) == False:
        A = pivoting(A)
        if domination(A) == False:
            print("אין אלכסון דומיננטי")
            return False
    return True


def Jacobi(matrixA, vectorB):
    num_of_iterations = 1000000
    if not check(matrixA):
        num_of_iterations = 100
    e = 1
    x0 = 0
    y0 = 0
    z0 = 0
    index = 1
    while (e >= eps and num_of_iterations > 0):
        x1 = (vectorB[0] - matrixA[0][1] * y0 - matrixA[0][2] * z0) / matrixA[0][0]
        y1 = (vectorB[1] - matrixA[1][0] * x0 - matrixA[1][2] * z0) / matrixA[1][1]
        z1 = (vectorB[2] - matrixA[2][0] * x0 - matrixA[2][1] * y0) / matrixA[2][2]

        print(index, '%0.6f\t%0.6f\t%0.6f\t' % (x1, y1, z1))

        e = abs(x1 - x0)
        x0 = x1
        y0 = y1
        z0 = z1

        index = index + 1
        num_of_iterations = num_of_iterations - 1

    print('\nSolution: x = %0.6f, y = %0.6f and z = %0.6f\n' % (x1, y1, z1))


def GaussSeidel(matrixA, vectorB):
    num_of_iterations = 1000000
    if not check(matrixA):
        num_of_iterations = 100
    e = 1
    x0 = 0
    y0 = 0
    z0 = 0
    index = 1
    while (e >= eps and num_of_iterations > 0):
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

    print('\nSolution: x = %0.6f, y = %0.6f and z = %0.6f\n' % (x1, y1, z1))


eps = 0.00001
matrixA = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
vectorB = [2, 6, 5]

c = input("Choose an option:\n1 - Jacobi\n2 - Gauss Siedel\n>>> ")
if c == '1':
    Jacobi(matrixA, vectorB)
elif c == '2':
    GaussSeidel(matrixA, vectorB)
else:
    print("Wrong input")

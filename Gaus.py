A = [[2, 5, 9, 16], [6, 7, 1, 14], [0, 3, 2, 5]]


def Mul_Matrix(A, B):
    # צריך לשנות לפי הגודל המתאים
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


def OrderPivot(A, col):
    max = abs(A[col][col])
    row_index = col
    for i in range(len(A)):
        if i >= col:
            if abs(A[i][col]) > max:
                max = A[i][col]
                row_index = i

    tmp = A[row_index]
    A[row_index] = A[col]
    A[col] = tmp


def Gaussian_Elimination(A):
    import os
    fileName = "Output"
    currentDirectory = os.getcwd()
    filePath = currentDirectory + "\\" + fileName

    E = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    try:
        with open(filePath, 'w', encoding='utf8') as f:
            for i in range(len(A)):
                for j in range(len(A)):
                    E = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
                    OrderPivot(A, j)
                    if j >= i:
                        if i == j:
                            E[j][i] = 1 / A[j][i]
                            for r in E:
                                f.write(str(r))
                                f.write("\n")
                            f.write("*\n")
                            for r in A:
                                f.write(str(r))
                                f.write("\n")
                            f.write("=\n")
                            A = Mul_Matrix(E, A)
                            for r in A:
                                f.write(str(r))
                                f.write("\n")
                            f.write("####################\n\n")
                        else:
                            E[j][i] = - A[j][i] / A[i][i]
                            for r in E:
                                f.write(str(r))
                                f.write("\n")
                            f.write("*\n")
                            for r in A:
                                f.write(str(r))
                                f.write("\n")
                            f.write("=\n")
                            A = Mul_Matrix(E, A)
                            for r in A:
                                f.write(str(r))
                                f.write("\n")
                            f.write("####################\n\n")

            for i in range(len(A)):
                for j in range(len(A)):
                    E = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
                    if j < i:
                        E[j][i] = - A[j][i] / A[i][i]
                        for r in E:
                            f.write(str(r))
                            f.write("\n")
                        f.write("*\n")
                        for r in A:
                            f.write(str(r))
                            f.write("\n")
                        f.write("=\n")
                        A = Mul_Matrix(E, A)
                        for r in A:
                            f.write(str(r))
                            f.write("\n")
                        f.write("####################\n\n")

            print(f"\nData written to file successfully!\nFile path: {filePath}\n")
            sol = [0, 0, 0]
            for i in range(len(A)):
                sol[i] = A[i][len(A)]
            return sol

    except OSError as err:
        print(f"Error! cannot open the file. {err}.")
        exit()
    except BaseException as err:
        print(f"Unexpected {err}, {type(err)}")
        raise


sol = Gaussian_Elimination(A)
print("Solution:", sol)

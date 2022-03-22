A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# B = [[1, 0, 0], [-4, 1, 0], [0, 0, 1]]
# sol = [1, 2, 3]


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
                    if j >= i:
                        if i == j:
                            if A[j][i] != 0:  # TODO check case of division by zero
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
                        if A[i][i] != 0:  # TODO check case of division by zero
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

            print(f"Data written to file successfully!\nFile path: {filePath}\n")

    except OSError as err:
        print(f"Error! cannot open the file. {err}.")
        exit()
    except BaseException as err:
        print(f"Unexpected {err}, {type(err)}")
        raise


Gaussian_Elimination(A)

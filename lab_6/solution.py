import copy
import numpy as np


def Gauss(matrix):
    n = len(matrix)
    matrix = GaussFoward(matrix)
    
    if Determinant(matrix) == 0:
        print("система має безліч розв'язків")
        return
    
    return GaussBack(matrix)


def GaussFoward(matrix):
    matrix = copy.deepcopy(matrix)
    n = len(matrix)
    for k in range(n - 1):
        if round(matrix[k][0] == 0.00):
            for i in range(k, n):
                if matrix[i][k] != 0:
                    matrix[i], matrix[k] = matrix[i], matrix[k] 
        for i in range(k + 1, n):
            mutipier = matrix[i][k] / matrix[k][k]    
            for j in range(k, n + 1):
                matrix[i][j] -= mutipier * matrix[k][j] 
    return matrix 

def GaussBack(matrix):
    matrix = copy.deepcopy(matrix)
    n = len(matrix)
    result = [0 for i in range(n)] 
    for k in range(n - 1, -1, -1):
        b = matrix[k][-1]
        sumOfRowOnX = sum([matrix[k][j] * result[j] for j in range(0, n)])
        result[k] = (b - sumOfRowOnX) / matrix[k][k]
    return result


def IsSingular(m):
    for i in range(len(m)):
        if m[i][i] == 0:
            return True
    return False

def Determinant(matrix):
    matrix = copy.deepcopy(matrix)
    determinant = 0
    matrix = GaussFoward(matrix)
    n = len(matrix)
    for i in range(0, n):
        determinant += matrix[i][i]
    return determinant

def GaussInverse(M):
    n = len(M)
    matrix = M 
    M = [[0 for i in range(n)] for i in range(n)]
    for i in range(0 , len(matrix)):
        for j in range(0, len(matrix)):
            M[i][j] = matrix[i][j]
    I = [[0 for i in range(n)] for i in range(n)]
    for i in range(n): I[i][i] = 1
    
    for i in range(n):
        j = i
        while M[j][i] == 0:
            j += 1
        M[i], M[j] = M[j], M[i]
        I[i], I[j] = I[j], I[i]
        const = M[i][i]
        for j in range(n): 
            I[i][j] = I[i][j] / const
            M[i][j] = M[i][j] / const

        for j in range(i+1,n): 
            const = M[j][i]
            for k in range(n):
                I[j][k] -= const * I[i][k]
                M[j][k] -= const * M[i][k]
    
    result = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        m = copy.deepcopy(M)
        for j in range(n):
            m[j].append(I[j][i])
        rowX = GaussBack(m)
        for j in range(n):
            result[j][i] = rowX[j]
    return result



def Progon(matrix):
    matrix = copy.deepcopy(matrix)
    coef = {"a" : [0.], "b" : [], "c" : [], "d" : [], "P" : [], "Q" :[]}
    for i in range(1, len(matrix)):
        coef["a"].append(matrix[i][i - 1])
    for i in range(0, len(matrix)):
        coef["b"].append(matrix[i][i])
    for i in range(0, len(matrix) -1):
        coef["c"].append(matrix[i][i + 1])
    coef["c"].append(0.0)
    for i in range(0, len(matrix)):
        coef["d"].append(matrix[i][-1])
    coef["P"].append(- coef["c"][0] / coef["b"][0]) 
    for i in range(1, len(matrix)):
        coef["P"].append( - coef["c"][i] / (coef["b"][i] + coef["a"][i] * coef["P"][i - 1]))
    
    coef["Q"].append(coef["d"][0] / coef["b"][0])
    for i in range(1, len(matrix)):
        coef["Q"].append((coef["d"][i] - coef["a"][i] * coef["Q"][i - 1]) / (coef["b"][i] + coef["a"][i] * coef["P"][i - 1]))
    result = [coef["Q"][-1]]
    for i in range(len(matrix) - 2, -1, -1):
        result.append(coef["P"][i] * result[-1] + coef["Q"][i])
    result.reverse()
    return result


def Zeidel(M, b, e):
    n = len(M)
    x = [.0 for i in range(n)]
    converge = False
    while not converge:
        xNew = np.copy(x)
        for i in range(n):
            sum1 = sum(M[i][j] * xNew[j] for j in range(i))
            sum2 = sum(M[i][j] * x[j] for j in range(i + 1, n))
            xNew[i] = (b[i] - sum1 - sum2) / M[i][i]
        converge = abs(sum(xNew[i] - x[i] for i in range(n))) <= e
        x = xNew
    return x

def SimpleIteration(matrix, e):
    n = len(matrix)
    matrix = copy.deepcopy(matrix)
    a = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i != j):
                a[i][j] = - matrix[i][j] / matrix[i][i]
    b = [matrix[i][-1] / matrix[i][i] for i in range(n)]
    
    maxSum = 0
    for i in range(n):
        s = 0
        for j in range(n):
            s += a[j][i]
        if abs(s) >= maxSum:
            maxSum = abs(s)
    result = copy.deepcopy(b)
    nextVector = MultipleMatrix(a, b)
    for i in range(n):
            nextVector[i] += b[i]
    while (maxSum/ (1 - maxSum)) * max([abs(result[i] - nextVector[i]) for i in range(n)]) >= e:
        result = copy.deepcopy(nextVector)
        nextVector = MultipleMatrix(a, result)
        for i in range(n):
            nextVector[i] += b[i]
    return result
    

     

def MultipleMatrix(matrix_1, matrix_2):
    n = len(matrix_1)
    m1 = copy.deepcopy(matrix_1)
    m2 = copy.deepcopy(matrix_2)
    resutl = []
    for i in range(n):
        resutl.append(0)
        for j in range(n):
            resutl[-1] += m1[i][j] * m2[j]
    return resutl

def Zeidel(matrix, e):
    n = len(matrix)
    matrix = copy.deepcopy(matrix)
    a = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i != j):
                a[i][j] = - matrix[i][j] / matrix[i][i]
    b = [matrix[i][-1] / matrix[i][i] for i in range(n)]
    
    maxSum = 0
    for i in range(n):
        s = 0
        for j in range(n):
            s += a[j][i]
        if abs(s) >= maxSum:
            maxSum = abs(s)
    result = copy.deepcopy(b)
    nextVector = ZeidelMultipleMatrix(a, result, b)
    p = 1
    while ((maxSum ** p)/ (1 - maxSum)) * max([abs(result[i] - nextVector[i]) for i in range(n)]) >= e:
        result = copy.deepcopy(nextVector)
        nextVector = ZeidelMultipleMatrix(a, result, b)
    return result

def ZeidelMultipleMatrix(matrix_1, matrix_2, b):
    n = len(matrix_1)
    b = copy.deepcopy(b)
    m1 = copy.deepcopy(matrix_1)
    m2 = copy.deepcopy(matrix_2)
    resutl = []
    for i in range(n):
        resutl.append(b[i])
        for j in range(n):
            if (j < i):
                resutl[-1] += m1[i][j] * resutl[j]
            else:
                resutl[-1] += m1[i][j] * m2[j]
    return resutl


Array1 = [
    [9., -7., -1., 1., 55.],
    [2., 7., 3., -6., -66],
    [4., 7., -3., -7., -43.],
    [-9., -5., -1., -6., -24.]]

Array2 = [
    [-11.,  9.,   0.,   0.,   0., -158.],
    [  0., -8.,  -6.,   0.,   0.,   66.],
    [  0.,  6.,  15.,  -2.,   0.,  -45.],
    [  0.,  0.,   4.,   6.,  -1.,   24.],
    [  0.,  0.,   0.,  -7., -10.,   -1.]
]
    
Array3 = [
    [ 15.,   3.,  -5.,  -5.,   36.],
    [  7., -15.,  -6.,   1., -112.],
    [ -4.,   7., -19.,  -6.,   19.],
    [  3.,   0.,  -5.,   8.,  -23.]
]


print("Гаус: ")
print(Gauss(Array1))
print("Визначник матриці: ")
print(Determinant(Array1))
print("Обернена матриця: ")
print(np.array(GaussInverse(Array1)))

print("Метод прогону:")
print(Progon(Array2))

print("Метод простих ітерацій:")
print(SimpleIteration(Array3, 0.01))


print("Зейдель:")
print(Zeidel(Array3, 0.01))
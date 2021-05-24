import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def getDeterminant(x, y, functions):
    mainDiag = functions[0](x, y) * functions[1](x, y)
    diag = functions[2](x, y) * functions[3](x, y)
    return mainDiag - diag

def Newton(x, y, functions, derivatives, e):
    current_x, current_y = x, y
    next_x, next_y = x, y
    while True:
        J = getDeterminant(next_x, next_y, derivatives)
        A1 = getDeterminant(next_x, next_y, [functions[0], derivatives[1], derivatives[2], functions[1]])
        A2 = getDeterminant(next_x, next_y, [derivatives[0], functions[1], functions[0], derivatives[3]])
        next_x = current_x - (A1 / J)
        next_y = current_y - (A2 / J)
        if max(abs(current_x - next_x), abs(current_y - next_y)) <= e: break
        current_x, current_y = next_x, next_y
    return [next_x, next_y]

def Iteration(x, y, functions, e):
    current_x, current_y = x, y
    next_x, next_y = x, y
    while True:
        next_x = functions[0](next_x, next_y)
        next_y = functions[1](next_x, next_y)
        if max(abs(current_x - next_x),abs(current_y - next_y)) <= e: break
        current_x, current_y = next_x, next_y
    return [next_x, next_y]

def function_1(x, y):
    return np.e ** (x * y) + x - 5

def function_2(x, y):
    return x ** 2 - 5 * y - 1

def derivative_fucntion_1_by_x(x, y):
    return y * np.e ** x + 1

def derivative_fucntion_1_by_y(x, y):
    return x * np.e ** y

def derivative_fucntion_2_by_x(x, y):
    return 2 * x

def derivative_fucntion_2_by_y(x, y):
    return -5

def revers_fuction2(x, y):
    return (5 * y + 1) ** 0.5

def revers_fuction1(x, y):
    return math.log(5 - x) / x



value_x1 = [i * 0.01 for i in range(150, 250)]
value_y2 = [i * 0.01 for i in range(0, 100)]
value_x2 = [revers_fuction2(0, value_y2[i]) for i in range(0, 100)]
value_y1 = [revers_fuction1(value_x1[i], 0) for i in range(0, 100)]

plt.plot(value_x1,value_y1)
plt.plot(value_x2,value_y2)
plt.show()

x = 2
y = 0.5
e = 0.0001
derivatives = [
    derivative_fucntion_1_by_x, 
    derivative_fucntion_2_by_y, 
    derivative_fucntion_1_by_y, 
    derivative_fucntion_2_by_x
    ]
functions = [function_1, function_2]
iterFns = [revers_fuction2, revers_fuction1]

Newton_results = Newton(x, y, functions, derivatives, e)

print("Метод Ньютона")
print("x: ", Newton_results[0])
print("y: ", Newton_results[1])

Iteration_result = Iteration(x, y, iterFns, e)

print("\nМетод простої Ітерації")
print("x: ", Iteration_result[0])
print("y: ", Iteration_result[1])
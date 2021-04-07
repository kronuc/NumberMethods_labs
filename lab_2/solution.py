import numpy as np
import matplotlib.pyplot as plt
#lagrange
class LagrangeMethod:
    def __init__(self, values_x, function):
        self.function = function
        self.values_x = values_x
        self.values_y = [function(x) for x in values_x]

    def __call__(self, x):
        return self.Polinom(x)

    def Polinom(self, x):
        result = 0
        for j in range(len(self.values_y)):
            addition = 1
            for i in range(len(self.values_x)):
                if i != j:
                    addition *= (x - self.values_x[i])
                    addition /= (self.values_x[j] - self.values_x[i])
            result += self.values_y[j] * addition
        return result

class NevtonMethod:
    def __init__(self, values_x, function):
        self.function = function
        self.values_x = values_x
        self.values_y = [function(x) for x in values_x]
    
    def __call__(self, x):
        return self.Polinom(x)
    
    def Polinom(self, x):
        coef  = self.values_y.copy()
        n = len(self.values_y) 
        for j in range(1, n):
            for i in range(n - 1, j - 1, -1):
                coef[i] = (coef[i] - coef[i - 1]) / (self.values_x[i] - self.values_x[i - j])
        
        result = 0
        for i in range(0, n):
            addition = coef[i]
            for j in range(0, i):
                addition *= (x - self.values_x[j])
            result += addition
        return result

def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def findError(point, max_of_derivative, function, polinom, values_x):
    polinonError = (max_of_derivative / factorial(len(values_x)))
    print(polinonError)
    for x in values_x:
        polinonError *= point - x
    absolutError = abs(function(point) - polinom(point))
    print(absolutError)
    return  polinonError / absolutError 





#example
def function(x):
    return (x ** 2) * (np.e ** x)

values_x_1 = [-2, -1, 0, 1]
values_x_2 = [-2, -1, 0.2, 1]

l_polinom_1 = LagrangeMethod(values_x_1, function)
n_polinom_1 = NevtonMethod(values_x_1, function)
values_fror_plot_X = [x*0.01 for x in range(610, 900)]
values_fror_plot_1 = [l_polinom_1(x) for x in values_fror_plot_X]
values_fror_plot_2 = [n_polinom_1(x) for x in values_fror_plot_X]
values_fror_plot_3 = [function(x) for x in values_fror_plot_X]

plt.plot(values_fror_plot_X, values_fror_plot_1)
plt.plot(values_fror_plot_X, values_fror_plot_2)
plt.plot(values_fror_plot_X, values_fror_plot_3)
plt.show()

l_polinom_2 = LagrangeMethod(values_x_2, function)
n_polinom_2 = NevtonMethod(values_x_2, function)

values_fror_plot_X = [x*0.01 for x in range(610, 900)]
values_fror_plot_1 = [l_polinom_2(x) for x in values_fror_plot_X]
values_fror_plot_2 = [n_polinom_2(x) for x in values_fror_plot_X]
values_fror_plot_3 = [function(x) for x in values_fror_plot_X]

plt.plot(values_fror_plot_X, values_fror_plot_1)
plt.plot(values_fror_plot_X, values_fror_plot_2)
plt.plot(values_fror_plot_X, values_fror_plot_3)
plt.show()


test_point = 0.5
print(findError(test_point, 21*np.e, function, n_polinom_1, values_x_1))
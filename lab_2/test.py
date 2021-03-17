import numpy as np

#lagrange
class LagrangeMethod:
    def __init__(self, values_x, function):
        self.function = function
        self.values_x = values_x
        self.values_y = [function(x) for x in values_x]

    def __call__(self, x):
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


#example
def function(x):
    return (x ** 2) * (np.e ** x)

values_x_1 = [-2, -1, 0, 1]
values_x_2 = [-2, -1, 0.2, 1]

polinom_1 = LagrangeMethod(values_x_1, function)
print(polinom_1(-2), function(-2))


polinom_2 = LagrangeMethod(values_x_2, function)
print(polinom_2(0.2), function(0.2))

test_point = 0.5
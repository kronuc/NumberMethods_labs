import math


class Euler_method:
    def __init__(self, our_range, step, y_0, y_der_0, accurate_function, y_second_derivative):
        self.our_range = our_range
        self.x = [round(our_range[0] + step * i, 2) for i in range(int((our_range[1] - our_range[0]) / step) + 1)]
        self.y = [y_0]
        self.y_der = [y_der_0]
        self.accurate_function = accurate_function
        self.y_second_derivative = y_second_derivative
        self.step = step
        self.init_values()
        print(self.y)
        print(self.y_der)


    def init_values(self):
        for i in range(len(self.x)):
            self.y_der.append(self.y_der[-1] + self.y_second_derivative(self.x[i], self.y[i], self.y_der[i]) * self.step)
            self.y.append(self.y[i] + self.step * self.y_der[-2])

    def get_error_in_point(self, x):
        for i in range(len(self.x)):
            if x == self.x[i]: 
                return abs(self.y[i] - self.accurate_function(x))


class Euler_Koshi_method:
    
    def __init__(self, our_range, step, y_0, y_der_0, accurate_function, y_second_derivative):
        self.our_range = our_range
        self.x = [round(our_range[0] + step * i, 2) for i in range(int((our_range[1] - our_range[0]) / step) + 1)]
        self.y = [y_0]
        self.y_der = [y_der_0]
        self.accurate_function = accurate_function
        self.y_second_derivative = y_second_derivative
        self.step = step
        self.init_values()
        print(self.y)
        print(self.y_der)
    
    def init_values(self):
        for i in range(len(self.x) - 1):
            y_der_next = self.y_der[-1] + self.y_second_derivative(self.x[-1], self.y[-1], self.y_der[-1]) * self.step
            y_next = self.y[-1] +  self.y_der[-1] * self.step
            self.y_der.append(                                                                           
                    self.y_der[-1]                                                          
                    + (self.y_second_derivative(self.x[i-1], self.y[i-1], self.y_der[i-1])        
                    + self.y_second_derivative(self.x[i], y_next, y_der_next)) 
                    * self.step * 0.5
                )
            self.y.append(                                                                           
                    self.y[-1]                                                          
                    + (self.y_der[-1]        
                    + self.y_der[-2]) 
                    * self.step * 0.5
                )        
    
    def get_error_in_point(self, x):
        for i in range(len(self.x)):
            if x == self.x[i]: 
                return abs(self.y[i] - self.accurate_function(x))

# incoming data


our_range = [1, 2]
step = 0.1
y_0 = 1
y_der_0 = 1

def accurate_function(x):
    return (19 / 54) * (x ** 5) + 35 / (54 * x) - ((x ** 2) / 9) * math.log(x)


def y_second_derivative(x, y, z):
    #z - value of y first derivative
    return (3 * x * z + 5 * y + (x ** 2) * math.log(x)) / (x ** 2)

euler_method = Euler_method(our_range, step, y_0, y_der_0, accurate_function, y_second_derivative)


euler_koshi_method = Euler_Koshi_method(our_range, step, y_0, y_der_0, accurate_function, y_second_derivative)


for i in range(11):
    print(euler_method.get_error_in_point(round(1 + 0.1 * i, 2)))



for i in range(11):
    print(euler_koshi_method.get_error_in_point(round(1 + 0.1 * i, 2)))

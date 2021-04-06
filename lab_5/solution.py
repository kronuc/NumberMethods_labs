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


class Adams_method:
    
    def __init__(self, our_range, step, y_0, y_der_0, accurate_function, y_second_derivative):
        self.our_range = our_range
        self.x = [round(our_range[0] + step * i, 2) for i in range(int((our_range[1] - our_range[0]) / step) + 1)]
        self.y = [y_0]
        self.y_der = [y_der_0]
        self.accurate_function = accurate_function
        self.y_second_derivative = y_second_derivative
        self.step = step
        self.q = [0 for i in range(len(self.x))]
        self.q_der = [0 for i in range(len(self.x))]
        self.init_values()
        print(self.y)
        print(self.y_der)
        print(self.q)
        print(self.q_der)
    
    def init_values(self):
        for i in range(4):
            self.y_der.append(self.y_der[-1] + self.y_second_derivative(self.x[i], self.y[i], self.y_der[i]) * self.step)
            self.y.append(self.y[i] + self.step * self.y_der[-2])
            self.init_q_der(i)
            self.init_q(i)

        for i in range(4, len(self.x)):
            self.count_y_der_with_q(i)
            self.count_y_with_q(i)
            self.init_q_der(i)
            self.init_q(i)
            



    def init_q_der(self, number):
        self.q_der[number] = self.y_second_derivative(self.x[number], self.y[number], self.y_der[number]) * self.step
        
        
    def init_q(self, number):
        self.q[number] = self.y_der[number] * self.step
        
    def count_y_der_with_q(self, number):

        self.y_der.append( \
            self.y_der[number - 1] \
            + (55 / 24) * self.q_der[number - 1] \
            - (59 / 24) * self.q_der[number - 2] \
            + (37 / 24) * self.q_der[number - 3] \
            - (9 / 24) * self.q_der[number - 4]
            )
    
    def count_y_with_q(self, number):
        self.y.append( \
            self.y[number - 1] \
            + (55 / 24) * self.q[number - 1] \
            - (59 / 24) * self.q[number - 2] \
            + (37 / 24) * self.q[number - 3] \
            - (9 / 24) * self.q[number - 4]
            )

    def get_error_in_point(self, x):
        for i in range(0, len(self.x)):
            if x == self.x[i]:
                return abs(self.y[i] - self.accurate_function(x))

        
# incoming data


our_range = [1, 2]
step = 0.1
y_0 = 1
y_der_0 = 1

def accurate_function(x):
    return (19 / 54) * (x ** 5) + (35 / (54 * x)) - ((x ** 2) / 9) * math.log(x)

def y_second_derivative(x, y, z):
    #z - value of y first derivative
    return (3 * x * z + 5 * y + (x ** 2) * math.log(x)) / (x ** 2)

euler_method = Euler_method(our_range, step, y_0, y_der_0, accurate_function, y_second_derivative)


adams_method = Adams_method(our_range, step, y_0, y_der_0, accurate_function, y_second_derivative)


for i in range(11):
    print(euler_method.get_error_in_point(round(1 + 0.1 * i, 2)))



for i in range(11):
    print(adams_method.get_error_in_point(round(1 + 0.1 * i, 2)), adams_method.y[i], adams_method.accurate_function(round(1 + 0.1 * i, 2)))
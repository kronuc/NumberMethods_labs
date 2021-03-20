import numpy as np
import matplotlib.pyplot as plt


class Equation:
    def __init__(self, values_x, values_y):
        self.values_x = values_x
        self.values_y = values_y
        self.intervals = [(values_x[i - 1],values_x[ i ]) for i in range(1, len(values_x))]
        self.values_h = 1
        self.CountQ()
    
    def CountQ(self):
        amountOfX = len(self.values_x)

        self.Qs = [0 for i in range(amountOfX)]
        coef = [{"a": 0, "b":0, "c":0, "d":0, "B":0, "A":0 } for i in range(amountOfX)]
        coef[1]["a"] = 0
        coef[amountOfX - 2]["c"] = 0
        
        for i in range(1, amountOfX - 1):
            coef[i]["d"] = (self.values_y[i + 1] - self.values_y[i]) / self.values_h
            coef[i]["d"] -= (self.values_y[i] - self.values_y[i - 1]) / self.values_h
        
        for i in range(2, amountOfX - 1):
            coef[i]["a"] = self.values_h / 6
        
        for i in range(1, amountOfX - 1):
            coef[i]["b"] = (2 * self.values_h) / 3
        
        for i in range(1, amountOfX - 2):
            coef[i]["c"] = self.values_h / 6
        
        coef[1]["A"] = coef[1]["c"] / coef[1]["b"] 
        for i in range(2, amountOfX - 1):
            coef[i]["A"] = coef[i]["c"] / (coef[i]["b"] + coef[i]["a"] * coef[i - 1]["A"])
        
        coef[1]["B"] = coef[1]["d"] / coef[i]["b"]
        for i in range(2, amountOfX - 1):
            coef[i]["B"] = (coef[i]["d"] - coef[i]["a"] * coef[i - 1]["B"]) / (coef[i]["b"] + coef[i]["a"] * coef[i - 1]["A"])
        
        for i in range(amountOfX - 2, 0, -1):
            self.Qs[i] = coef[i]["A"] * self.Qs[i + 1] + coef[i]["B"]

    def __call__(self, x):

        if x < self.intervals[0][0]:
            return self.CountForInterval(x, 0)
        if x > self.intervals[len(self.intervals) - 1][1]:
            return self.CountForInterval(x, len(self.values_x) - 2)
        for i in range (0, len(self.intervals)):
            if x >= self.intervals[i][0] and x <= self.intervals[i][1]:
                return self.CountForInterval(x, i)

    def CountForInterval(self, x, intervalNumber):
        i = intervalNumber
        return  - (
            (((self.Qs[i] * (self.values_x[i + 1] - x) ** 3) / 6 * self.values_h)) +  
            ((self.Qs[i + 1] * (x - self.values_x[i]) ** 3) / 6 * self.values_h) +
            (((self.values_y[i] / self.values_h) - self.Qs[i] * (self.values_h / 6)) * (self.values_x[i + 1] - x)) + 
            (((self.values_y[i + 1] / self.values_h) - self.Qs[i + 1] * (self.values_h / 6)) * (x - self.values_x[i]))
            )
            




#example
x = [-1.2, -0.7, -0.2, 0.3, 0.8]
y = [0.43372, 0.24333, 0.032749, 0.12149, 1.4243]
point = -0.5
equaition = Equation(x, y)

values_fror_plot_X = [x*0.1 for x in range(10, 50)]
values_fror_plot_1 = [equaition(x) for x in values_fror_plot_X]
plt.plot(values_fror_plot_X, values_fror_plot_1)
plt.show()
print(equaition(point))

import math

def areDifferent(func, a, b):
    if func(a) >= 0 and func(b) <= 0:
        return True
    elif func(a) <= 0 and func(b) >= 0:
        return True
    else:
        return False

def isGrowing(funktion, segment):
    return funktion(segment[1]) - funktion(segment[0]) > 0  

def halfDivisionMethod(function, segment, deviation):
    if not areDifferent(function, segment[0], segment[1]):
        return None
    lower = segment[0]
    higer = segment[1]
    midle = (lower + higer) / 2 
    if not isGrowing(function, segment):
        lower = segment[1]
        higer = segment[0]
    while function(higer)-function(lower) > 2 * deviation:
        if function(midle) == 0:
            break
        elif function(midle) < 0:
            lower = midle
            midle = (lower + higer) / 2 
        else: 
            higer = midle
            midle = (lower + higer) / 2 
    return midle

def newtonMethod(function, functionSignature, current, deviation):
    next = current - function(current) / functionSignature(current)
    while abs(function(next) - function(current)) > deviation:
        current = next
        next = current - function(current) / functionSignature(current)
    return next    

def iterationMethod(funuction, number, deviation):
    current = number
    next = funuction(number)
    while abs(current - next) > deviation:
        current = next 
        next = funuction(current)
    return next
seg_1 = [-1.0, 0.0]
seg_2 = [0.0, 1.0]
def example(x):
    return x**5 - 7 * x**2 + 3

def exampleSignature(x):
    return 5 * x**4 - 14 * x 

def exampleRevers_1(x):
    return -(-3 / (x**3 - 7))**0.5


def exampleRevers_2(x):
    return (-3 / (x**3 - 7))**0.5


print("half division method")
print(halfDivisionMethod(example, seg_1, 0.00001))
print(halfDivisionMethod(example, seg_2, 0.00001), "\n")

print("newton nethod")
print(newtonMethod(example, exampleSignature, -0.6, 0.00001))
print(newtonMethod(example, exampleSignature, 0.6, 0.00001), "\n")

print("iteration method")
print(iterationMethod(exampleRevers_1, -0.6, 0.00001))
print(iterationMethod(exampleRevers_2, 0.6, 0.00001), "\n")
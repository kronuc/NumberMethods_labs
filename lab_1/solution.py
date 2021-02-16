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

seg = [-1.0, 0.0]

def example(x):
    return x**5 - 7 * x**2 + 3

print(halfDivisionMethod(example, seg, 0.00001))

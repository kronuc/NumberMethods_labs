def runge(function, method_function, a , b, h):
    with_full_h = method_function(function, a, b, h)
    with_half_of_h = method_function(function, a, b, h / 2)

    result = with_half_of_h - ((with_half_of_h - with_full_h) / 3)
    return result 

def rectangular(function, a, b, h):
    x = a + h / 2 
    result = 0
    while x <= b:
        result += h * function(x)
        x += h
    return result

def simpson(function, a, b, h):
    result = function(a) + function(b)
    x = a + h
    while x < b:
        result += 4 * function(x)
        x += 2 * h
    x = a + 2 * h
    while x < b:
        result += 2 * function(x)
        x += 2 * h
    result *= h/3
    return result

def trapezoidal(function, a, b, h):
    result = 0
    x = a + h
    while x <= b:
        result += (function(x) + function(x - h)) * h * 0.5
        x += h
    return result



#testing
def function(x):
    return (x ** 2 - 36) ** 0.5

a = 6.5
b = 8.5
h1 = 0.5
h2 = 0.25
print("count with h =", h1)
print("rectangular method:", rectangular(function, a, b, h1))
print("rectification:", runge(function, rectangular, a, b, h1))
print()
print("trapezoidal method:", trapezoidal(function, a, b, h1))
print("rectification:", runge(function, trapezoidal, a, b, h1))
print()
print("Simpson`s method:", simpson(function, a, b, h1))
print("rectification:", runge(function, simpson, a, b, h1))
print()
print("count with h =", h2)
print("rectangular method:", rectangular(function, a, b, h2))
print("rectification:", runge(function, rectangular, a, b, h2))
print()
print("trapezoidal method:", trapezoidal(function, a, b, h2))
print("rectification:", runge(function, trapezoidal, a, b, h2))
print()
print("Simpson`s method:", simpson(function, a, b, h2))
print("rectification:", runge(function, simpson, a, b, h2))
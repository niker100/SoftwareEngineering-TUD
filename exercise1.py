#  1. Write the Python code to calculate Earth's orbit. Hint: assume the orbit is a circle with a radius of 150 million
# km.
def e1():
    import math
    r = 150000000
    c = 2 * math.pi * r
    return c

print(f'The circumference of Earth\'s orbit is {e1()} km')

#  2. Find the sum of the terms of an arithmetic progression: a, a+d, a+2*d, … , a+n*d
#  based on given values a, d, and n.
def e2_iterative(a, d, n):
    s = 0
    for i in range(n + 1):
        s += a + i * d
    return s
def e2_recursive(a, d, n):
    if n == 0:
        return a
    return a + n * d + e2_recursive(a, d, n - 1)

def e2_algebraic(a, d, n):
    return (n +1) * (2 * a + n * d) / 2

print(f'iterative: {e2_iterative(1, 2, 3)} '
      f'recursive: {e2_recursive(1, 2, 3)} '
      f'algebraic: {e2_algebraic(1, 2, 3)}')

#  3. Calculate the distance between two points with coordinates X1, Y1 and X2, Y2
def e3(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(e3(1, 1, 4, 5))

# 4. The variables A, B, and C contain the lengths of the sides of a triangle. Calculate its area and store the result
# in the variable S.
# Heron's formula
def e4(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

S = e4(3, 4, 5)
print(S)

# 5. Swap the values of two variables without using a third variable.
def e5(a, b):
    a, b = b, a
    return a, b

print(e5(1, 2))

# 6. Raise the number A to the fifth power and to the sixteenth power.
def e6(a):
    return a ** 5, a ** 16

print(e6(2))

#  7. The variable X contains a three-digit integer. Store the sum of its digits in the variable S.
def e7(x):
    return sum([int(i) for i in str(x)])

S = e7(123)
print(S)

#  8. A real number X is given (-1 <= X <= 1). Calculate the value of the arcsin function using the math library.
def e8(x):
    import math
    return math.asin(x)

print(e8(0.5))

#  9. A real number X is given. Calculate the value of a polynomial 2x^4 − 3x^3 + 4x^2 − 5x + 6, performing as few
# arithmetic operations as possible.
def e9(x):
    return 2 * x ** 4 - 3 * x ** 3 + 4 * x ** 2 - 5 * x + 6

def e9_horner(x):
    return 6 + x * (-5 + x * (4 + x * (-3 + 2 * x)))

print(e9(2))
print(e9_horner(2))

# Algebra Operations

def add(a, b):
    """Addition"""
    return a + b

def subtract(a, b):
    """Subtraction"""
    return a - b

def multiply(a, b):
    """Multiplication"""
    return a * b

def divide(a, b):
    """Division"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exp):
    """Exponentiation"""
    return base ** exp

def square_root(x):
    """Square Root"""
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    return x ** 0.5

def quadratic_roots(a, b, c):
    """Solve quadratic equation ax^2 + bx + c = 0"""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return (root1, root2)

def factorial(n):
    """Factorial of n"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def gcd(a, b):
    """Greatest Common Divisor"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Least Common Multiple"""
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    print("Addition 3+5:", add(3, 5))
    print("Subtraction 10-4:", subtract(10, 4))
    print("Multiplication 6*7:", multiply(6, 7))
    print("Division 20/4:", divide(20, 4))
    print("Power 2^10:", power(2, 10))
    print("Square Root of 144:", square_root(144))
    print("Quadratic roots of x^2 - 5x + 6:", quadratic_roots(1, -5, 6))
    print("Factorial of 5:", factorial(5))
    print("GCD of 12 and 18:", gcd(12, 18))
    print("LCM of 4 and 6:", lcm(4, 6))

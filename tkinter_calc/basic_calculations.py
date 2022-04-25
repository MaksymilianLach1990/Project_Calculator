# Basic calculations

# Add
def add(a, b):
    result = a + b
    return result

# Subtract
def subtract(a, b):
    result = a - b
    return result

# Multiplication
def multiplication(a, b):
    result = a * b
    return result

# Division
def division(a, b):
    result = a / b
    return result

# Raising to power
def exponentiation(a, b):
    result = a ** b
    return result

# The rest from division
def modulo(a, b):
    result = a % b
    return result

# Division without change
def excellence(a, b):
    result = a // b
    return result

# Element
def element(a, b):
    result = a ** (1/b)
    return result

# Check action
def check_action(num_a, num_b, action):
    
    options = {
        '+': add,
        '-': subtract,
        '*': multiplication,
        '/': division,
        '**': exponentiation,
        '%': modulo,
        '√': element
    }

    return options[action](float(num_a), float(num_b))

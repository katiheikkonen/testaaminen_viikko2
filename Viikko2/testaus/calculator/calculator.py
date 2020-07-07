def plus(a, b):
    try:
        return a + b
    except TypeError as e:
        raise e("Only numbers are allowed")

def minus(a, b):
    try:
        return a - b
    except TypeError as e:
        raise e("Only numbers are allowed")

def multiplication(a, b):
    return float(a * b)

def division(a, b):
    try:
        return a / b
    except TypeError as e:
        raise e("Only numbers are allowed")


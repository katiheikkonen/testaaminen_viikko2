#  FIZZBUZZ

def fizzbuzz(num):
    if num < 0:
        raise ValueError
    elif isinstance(num, float):
        raise ValueError
    else:
        try:
            if num % 5 == 0 and num % 3 == 0:
                return 'FizzBuzz'
            elif num % 5 == 0:
                return 'Fizz'
            elif num % 3 == 0:
                return 'Buzz'
            else:
                return num
        except TypeError as e:
            raise e("Only numbers are allowed")

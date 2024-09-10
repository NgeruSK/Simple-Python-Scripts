import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took "+ str((end-start)*1000) + " mil seconds")
        return result
    return wrapper

@time_it
def calc_squares(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cubes(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result


calc_cubes(range(1,90000))
calc_squares(range(1,100000))
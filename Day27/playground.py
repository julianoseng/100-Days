def add(*args):
    sum_nums = 0
    for num in args:
        sum_nums += num
    return sum_nums


print(add(3, 5, 6, 7, 8))

# Keyword arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]


calculate(2, add=3, multiply=5)
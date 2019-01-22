from sympy import *


def get_series(n):
    x = Symbol('x')
    series = x

    for i in range(2, n + 1):
        series = series + (x ** i) / i

    return series


def print_series(n):
    init_printing(order='rev-lex')
    pprint(get_series(n))


n = input('Enter the number of terms you want in the series: ')
print_series(int(n))

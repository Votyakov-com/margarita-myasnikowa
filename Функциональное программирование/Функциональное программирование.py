#задача 1
def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n-1)*n
print(factorial(int(input())))

#задача 2


def is_prime(n,d=2):
    if n ==1:
        return False
    if n == d:
        return True
    if (n%d == 0) :
        return False
    new_d=d+1
    return is_prime(n,new_d)

print(is_prime(int(input())))

#задача 3
def filter_odd(numbers):
    return (list(filter(lambda x:x%2!=0, numbers)))
print(filter_odd(list(map(int, input().split()))))

#задача 4

def map_square(numbers):
    return list(map(lambda x:x**2,numbers))
print(map_square(list(map(int, input().split()))))

#задача 5
from functools import  reduce
def reduce_sum(numbers):
    return reduce(lambda x,y:x+y,numbers)
print(reduce_sum([1,2,3,4,5]))

#задачв 6
def anything_func(x,y):
    return x+y
def partial_apply(func,x):
    def partical_func(y):
        return func(x,y)
    return partical_func
one_sum = partial_apply(anything_func, 1)
print(one_sum(3))

#задача 7

def compose(f,g):
    def h(x):
        return g(f(x))
    return h
#задача 8
def create_function_with_arguments(func, *arguments):
    def new_func():
        return func(arguments)
    return new_func
#задача 9
def compose_functions(*functions):
    def composed_function(x,num=0):
        if num>=len(functions):
            return x
        iter_func = functions[num](x)
        new_num = num+1
        return compose_function(iter_func,new_num)
    return composed_function




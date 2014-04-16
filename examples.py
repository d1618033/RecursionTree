from recursion_tree import recursion_tree
from random import choice

@recursion_tree(save_to_file=True)
def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


@recursion_tree(save_to_file=True)
def permutations(array, soFar=None):
    if soFar is None:
        soFar = []
    if len(array) == 0:
        print(soFar)
    else:
        for index, value in enumerate(array):
            permutations(array[:index] + array[index+1:], soFar + [value])


@recursion_tree(save_to_file=True)
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

@recursion_tree(save_to_file=True)
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = choice(array)
    left = quick_sort([a for a in array if a < pivot])
    right = quick_sort([a for a in array if a > pivot])
    middle = [a for a in array if a == pivot]
    return left + middle + right


@recursion_tree(save_to_file=False)
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0:
        if n == 0:
            return ackermann(m - 1, 1)
        else:
            return ackermann(m - 1, ackermann(m, n - 1))


ackermann(2, 2)
ackermann(1, 1)
quick_sort([1, 9, 2, 4, 8, 6, 10, 5, 3, 11])
fibo(7)
factorial(4)
permutations(['a', 'b', 'c'])

import timeit
import numpy

def sum_range(n=10000000):
    return sum(range(n))

def sum_numpy(n=10000000):
    return numpy.sum(numpy.arange(n))

def sum_math(n=10000000):
    return (n + (n - 1)) // 2 

def main():
    print('sum range\t\t', timeit.timeit(sum_range, number=1))
    print('sum numpy\t\t', timeit.timeit(sum_numpy, number=1))
    print('sum math\t\t', timeit.timeit(sum_math, number=1))

if __name__ == "__main__":
    main()
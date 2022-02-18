import timeit
import numpy

def for_loop(n=10000000):
    a = 0
    for x in range(n):
        a += x
    return a

def for_loop_increment(n=10000000):
    a = 0
    for x in range(n):
        a +=x
        x +=1
    return x

def sum_range(n=10000000):
    return sum(range(n))

def sum_numpy(n=10000000):
    return numpy.sum(numpy.arange(n))


def main():
    print('for loop \t\t', timeit.timeit(for_loop, number=1))
    print('for loop increment\t\t', timeit.timeit(for_loop_increment, number=1))
    print('sum numpy\t\t', timeit.timeit(sum_numpy, number=1))
    print('sum range\t\t', timeit.timeit(sum_range, number=1))

if __name__ == "__main__":
    main()
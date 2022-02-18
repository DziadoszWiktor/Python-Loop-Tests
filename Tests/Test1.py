import timeit

def while_loop(n=10000000):
    a = 0
    b = 0
    while a < n:
        b += a
        a += 1

def for_loop(n=10000000):
    a = 0
    for x in range(n):
        a += x
    return a

def main():
    print('while loop\t\t', timeit.timeit(while_loop, number=1))
    print('for loop\t\t', timeit.timeit(for_loop, number=1))

if __name__ == "__main__":
    main()
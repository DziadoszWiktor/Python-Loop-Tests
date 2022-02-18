import timeit

def for_loop_increment(n=10000000):
    a = 0
    for x in range(n):
        a +=x
        x +=1
    return x

def for_loop_test(n=10000000):
    a = 0
    for x in range(n):
        if x < n: pass
        a +=1
    return a

def for_loop_test_increment(n=10000000):
    a = 0
    for x in range(n):
        if x < n: pass
        x +=1
        a +=1
    return a

def main():
    print('for loop test\t\t', timeit.timeit(for_loop_test, number=1))
    print('for loop increment\t\t', timeit.timeit(for_loop_increment, number=1))
    print('for loop test increment\t\t', timeit.timeit(for_loop_test_increment, number=1))

if __name__ == "__main__":
    main()
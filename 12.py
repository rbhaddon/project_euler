''' This would probably be a lot faster without the prime calculation.
    Just count how many n % i == 0s.
'''

from operator import mul
from math import sqrt

def gen_triangle_nums():
    n = 1
    while True:
        yield n*(n+1)/2
        n += 1

def gen_primes():
    yield 2
    n = 3
    while True:
        is_prime = True
        for i in xrange(2, int(sqrt(n)) + 1):
            if not n % i:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1

def count_factors(num, f):
    ''' Returns how many times f can be evenly divided into num '''
    if num == f:
        return 1
    if num % f:
        return 0
    else:
        return 1 + count_factors(num/f, f)

def gen_factor_counts(source):
    ''' Generates the number of factors for each number in source.
        This is done by counting the number of times a prime can be divided
        into num.  For each count, add one then multiply them all together.
        Numbers 1, 2, 3 are special cases.  We dispatch 1 immediately, and
        deal with 2 and 3 with the initial value in the yield's reduce at 
        the bottom.
    '''
    gp = gen_primes()
    primes = [next(gp)]
    for num in source:
        # 1 is special case
        if num == 1:
            yield (num, 1)
            continue
        # Grow primes until highest prime is > sqrt(num)
        while primes[0] < sqrt(num) + 1:
            primes.insert(0, next(gp))
        # Count the factors
        factors = []
        for p in primes:
            p_count = count_factors(num, p)
            if p_count > 0:
                factors.append(p_count + 1)
        # The third arg to reduce handles nums = 2 or 3 special cases
        yield (num, reduce(mul, factors, 1 if factors else 2))

def problem_12():
    for (n, c) in gen_factor_counts(gen_triangle_nums()):
        if c > 500:
            print n, c
            break

from p7 import _gen_primes, _gen_possible_primes

def primes_below_n(num):
    primes = (x for x in _gen_primes(_gen_possible_primes()))
    p = next(primes)
    while p < num:
        yield p
        p = next(primes)

# Uncomment to solve, but it is very inefficient for large n
# print "Sum of primes under 2M:", sum(primes_below_n(2000000))

# Here's a faster prime number generator, based off a technique I saw in the 
# solution thread for problem #10.  It is at least an order of magnitude better
# than what I did for problem 7.
# My analysis:
#   My p7 solution executes in O(n**2), but flat memory usage.
#   This solution is linear for both execution and memory usage.
def another_primes_below_n(num):
    # first, get 2 out of the way
    yield 2
    
    # now find primes 3+
    primes = [True] * num
    value = 3
    while value < num:
        if primes[value]:
            yield value
            # Mark all multiples of value as non-prime:
            i = value
            while i < num:
                primes[i] = False
                i += value
        value += 2

print "Sum of primes under 2M:", sum(another_primes_below_n(2000000))

'''
    Problem 7, implemented witht the Sieve of Eratosthenes
'''

def _gen_possible_primes():
    ''' Bottomless pit of _potential_ prime numbers '''
    #yield 2
    x = 3
    while True:
        yield x
        x += 2
    
def _gen_primes(source):
    ''' Actual Sieve of Eratosthenes is here '''
    # Start with first prime
    primes = [2]
    for p in primes:
        yield p
    for s in source:
        s_is_prime = True
        for p in primes:
            #print "DEBUG: p =", p, "s =", s
            s_is_prime = s_is_prime and s % p
        if s_is_prime:
            primes.append(s)
            yield s

def nth_prime(num):
    primes = (x for x in _gen_primes(_gen_possible_primes()))
    for n, p in enumerate(primes):
        if n == num - 1:
            return p

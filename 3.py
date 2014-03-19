'''
    This is a flawed implementation of a largest prime factor finder.
    It sometimes returns non-prime factors for certain input values
    (like 160 or 180).

    Using sqrt(n) in the while loop is much faster, but still incorrect for
    certain input values (like 98 or 99).
'''
def max_prime_factor(num):
    def _max_prime_factor(n):
        f = 2
        while f < n / 2:
            if not n % f:
                n = n / f
            f += 1
        return n
    #import ipdb; ipdb.set_trace()
    return _max_prime_factor(int(num))

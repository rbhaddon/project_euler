''' 
    problem 9 - using Euclid's formula for generating pythagorean triples

    Euclid's Formula:
    Given two arbitrary integers m, n where m > n, form a triple with:
        a = m**2 - n**2, b = 2 * m * n, c = m**2 + n**2
'''

def gen_pyth_trip():
    # Start with first pythagorean triple (3, 4, 5)
    m = 2
    while True:
        for n in xrange(1, m):
            #print "DEBUG:", m, n
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            yield (a, b, c)
        m += 1

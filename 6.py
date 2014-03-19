# brute force
sums = 0
sum_sq = 0
for x in xrange(1,101):
    sums += x
    sum_sq += x**2

print sums**2 - sum_sq

# smarter
def sum_n(n):
    ''' Returns sum of [1..n] '''
    return n * (n + 1) / 2

def sum_sq_n(n):
    ''' Returns sum of [1**2..n**2] '''
    return (2 * n + 1) * (n + 1) * n / 6

print sum_n(100)**2 - sum_sq_n(100)

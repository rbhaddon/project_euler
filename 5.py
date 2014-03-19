# smallest common multiple of [1..10]:
# n = 2520
n = 2 * 2 * 2 * 3 * 5 * 7 * 3

# so smallest common multiple of [1..20] is the above plus additional prime
# factors to cover digits [11..20].  Thus:
n2 = (2 * 2 * 2 * 3 * 5 * 7 * 3) * 11 * 13 * 17 * 19 * 2
# Need to add the 2 at the end to cover 16 (2**4)

# test it
print n2, 'works:', not [x for x in xrange(1, 21) if n2 % x]

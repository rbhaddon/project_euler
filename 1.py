def multiples_3_5():
    for i in xrange(1000):
        if i % 3 == 0 or i % 5 == 0:
            yield i

print sum(multiples_3_5())

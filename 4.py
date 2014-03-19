def is_palindrome(num):
    ''' uses strings to test if num is palindromic '''
    num_str = str(num)
    return num_str == num_str[::-1]

def gen_palindromes():
    ''' generator of palindromic products of two three digit numbers
        Relies on the 'trick' that all palindromic numbers have 11 as a 
        prime factor.
    '''
    for i in xrange(999, 100, -1):
        for j in xrange(990, 100, -11):
            product = i * j
            if is_palindrome(product):
                yield product, i, j
 
print max([p for p, x, y in gen_palindromes()])

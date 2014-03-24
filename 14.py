''' Longest Collatz sequence -- PE problem 14
'''

memo = {}
def collatz_solver(num):
    ''' uses memoization '''
    ans = []
    n = num
    while n > 1:
        cached = memo.get(n)
        if cached is not None:
            memo[num] = ans + cached
            return ans + cached
        ans.append(n)
        n = (3 * n + 1) if n % 2 else (n / 2)
    ans.append(1)
    memo[num] = ans
    return ans
    
def collatz_solver_memoless(num):
    ''' does not use memoization '''
    ans = []
    n = num
    while n > 1:
        ans.append(n)
        n = (3 * n + 1) if n % 2 else (n / 2)
    ans.append(1)
    return ans
    
def problem_14():
    ''' On my mac book air:
        7.5s with memoization, 
        41.8s without memoization
    '''
    max = (0,0)
    solver = ((x,len(collatz_solver(x))) for x in xrange(1000000))
    #solver = ((x,len(collatz_solver_memoless(x))) for x in xrange(1000000))
    for n, l in solver:
        if l > max[1]:
            max = (n, l)
    print max

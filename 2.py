fib_memo = {0: 1, 1: 2}

def fibonacci(num):
    pre = fib_memo.get(num)
    if pre is not None:
        return pre
    else:
        new = fibonacci(num - 1) + fibonacci(num - 2)
        fib_memo[num] = new
        return new

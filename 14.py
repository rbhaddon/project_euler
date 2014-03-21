''' Longest Collatz sequence -- PE problem 14
'''

memo = {}

def collatz_solver(num):
    if num == 1:
        return num
    if num % 2:
        # odd
        return num, collatz_solver(3 * num + 1)
    else:
        # even
        return num, collatz_solver(num / 2)

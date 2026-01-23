def recursive_fib(n):
    return n if n <= 1 else recursive_fib(n - 1) + recursive_fib(n - 2)
print([recursive_fib(x) for x in range(0, 10)])

def iter_fib(n):
    seq = [0,1]
    for i in range(1, n):
        seq[i,  ]
def fib(n):
    phi = (1 + 5**0.5) / 2
    conj = 1 - phi
    return round((phi**n - conj**n) / (5**0.5))
print(fib(10))

def test_nth_fibonacci_number():
    print("Testing nth_fibonacci_number...", end="")
    assert(fib(1) == 1)
    assert(fib(3) == 2)
    assert(fib(7) == 13)
    assert(fib(10) == 55)
    print("... done!")
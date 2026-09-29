# Fibonacci Number Calculator

A short Python program that finds the **nth Fibonacci number** using a math formula (no loops, no recursion).

## What is the Fibonacci sequence?

Each number is the sum of the two numbers before it:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
```

So `fib(10)` gives `55`.

## How to run

1. Install Python 3.
2. Save the code in a file called `fibonacci.py`.
3. Run:

```bash
python fibonacci.py
```

Output:

```
55
```

## How the code works

```python
def fib(n):
    phi = (1 + 5**0.5) / 2
    conj = 1 - phi
    return round((phi**n - conj**n) / (5**0.5))
```

| Line | What it does |
|---|---|
| `phi = (1 + 5**0.5) / 2` | Calculates the golden ratio (about 1.618) |
| `conj = 1 - phi` | Calculates its partner value (about -0.618) |
| `return round(...)` | Plugs both into **Binet's formula** and rounds the result to a whole number |

The formula is:

```
F(n) = (phi^n - conj^n) / sqrt(5)
```

`round()` is used because computers store decimals approximately, so the raw result may look like `54.99999` instead of `55`.

## Testing

The program includes a test function that checks a few known values:

| Call | Expected |
|---|---|
| `fib(1)` | 1 |
| `fib(3)` | 2 |
| `fib(7)` | 13 |
| `fib(10)` | 55 |

To run the tests, add this line at the bottom of the file:

```python
test_nth_fibonacci_number()
```

If everything is correct, you will see:

```
Testing nth_fibonacci_number...... done!
```

Note: the test function is only defined in the code, so it does nothing until you call it.

**Tip:** the test function calls `fib`, so make sure the function name matches (`fib`, not `nth_fibonacci_number`).

## Limitations

- Works correctly only for `n` up to about **70**. After that, decimal precision errors give wrong answers.
- `n` should be a whole number that is 0 or higher.

For very large `n`, use a loop-based method instead:

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

## Summary

| Item | Detail |
|---|---|
| Language | Python 3 |
| Method | Binet's formula |
| Speed | Very fast (constant time) |
| Accurate up to | n ≈ 70 |
| Dependencies | None |

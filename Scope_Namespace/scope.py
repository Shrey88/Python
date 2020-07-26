# =============================================================================
# recursive function e.g. factorial
# =============================================================================


# def factorial(n):
#     """calculate n! recursively"""
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# for i in range(130):
#     print(i, factorial(i))


# ==========================================================================
# fibonacci series
# ==========================================================================


def fib(n):
    """F(n) = F(n-1) + F(n-2)"""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


for i in range(36):
    print(i, fib(i))

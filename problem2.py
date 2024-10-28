import sympy


def is_prime(some_number: int) -> bool:
    return sympy.isprime(some_number)

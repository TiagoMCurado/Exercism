""" Exercise sieve from exercism.
https://exercism.org/tracks/python/exercises/sieve"""


def primes(limit: int):
    """A program that uses the Sieve of Eratosthenes to find all the primes from 2 up to a given
    number.

    Parameters
    --------
    limit: int
    Highest number up to which the function of the sieve of Eratosthenes is used.

    Returns:
    prime_list = list[int]
    List with all the primes from 2 up to a given
    number (limit).
    """

    if limit == 1:
        return []

    candidates_list = list(
        range(2, limit + 1)
    )  # create a list with all integers from 2 to limit.

    primes_list = []

    while candidates_list:
        # while create a condition that happens until candidates_list is not empty.
        # If candidates_list is empty, while return False.
        p = min(candidates_list)
        primes_list.append(p)
        candidates_list.remove(p)

        for c in candidates_list:
            if c % p == 0:
                candidates_list.remove(c)

    return primes_list

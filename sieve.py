"""
make a sieve of eratosthenes
"""

def find_primes(n):
    multiples = []
    for i in range(2, n+1):

        for j in range(i*i, n+1, i):
            multiples.append(j)

    return [i for i in range(3, n) if i not in multiples]


print(find_primes(2000))

def prime(n=100):
    primes = [2, 3]

    for i in range(5, n):
        is_prime = 1
        for j in primes:
            if (i % j) == 0:
                is_prime = 0
                break
        if is_prime == 1:
            primes += [i]
    for p in primes:
        print p
    return 0



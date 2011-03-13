def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    D = {}  
    q = 2  
    while True:
        if q not in D:
            yield q        
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def gen_prime_pairs():
    prev_prime = -100
    for prime in gen_primes():
        if prime-prev_prime == 2:
            yield (prev_prime, prime)
        prev_prime = prime

i = 0
for k,v in gen_prime_pairs():
    print k,v
    i += 1
    if i>30:
        break

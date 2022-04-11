def generate_primes(n):
    primes = []
    is_prime = [False, False] + (n-1)*[True]
    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p*2, n+1, p):
                is_prime[i] = False
    return primes

n = 180
print(generate_primes(n))
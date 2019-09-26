import math

def primes(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0

    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]

if __name__ == '__main__':
    print(primes(10000)) 


def get_primes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def waiter(plates, q):
    primes = get_primes(10000)
    result = []
    for i in range(q):
        if not plates:
            break
        A = []
        B = []
        prime = primes[i]
        for plate in plates:
            if plate % prime == 0:
                B.append(plate)
            else:
                A.append(plate)
        result.extend(B)
        plates = A[::-1]
    result.extend(plates[::-1])
    return result


print(waiter([3, 3, 4, 4, 9], 2))
list_of_primes = []

for n in range(2, 101):
    if_prime = True
    for m in range(2, n-1):
        if n % m == 0:
            if_prime = False
            break
        list_of_primes.append(n)

set_of_primes = set(list_of_primes)
print(set_of_primes)
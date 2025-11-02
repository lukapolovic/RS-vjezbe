def isPrime(number):
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

print(isPrime(7))
print(isPrime(10))

def primes_in_range(start, end):
    primes = []
    for i in range(start, end+1):
        if isPrime(i):
            primes.append(i)
    return primes

print(primes_in_range(1, 10))
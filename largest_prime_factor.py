# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# returns True if parameter n is a prime number, False if composite and "Neither prime, nor composite" if neither
def isPrime(n):
    if n < 2: return "Neither prime, nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# returns smallest factor of parameter n
def findSmallestFactor(n):
    factor = 2 # start at the lowest possible factor
    while n % factor != 0: # go until factor is a factor
        if factor >= n** 0.5: # there is no factor if past square root point
            return n
        factor += 1 # test the next factor
    return factor

# reduces the parameter n into a product of only prime numbers
# and returns a list of those prime number factors
def primeFactorization(n):

    primes = [] # list of prime factors in the prime factorization
    largestFactor = n / findSmallestFactor(n)

    i = 2
    while i <= largestFactor: # for all possible prime factors (2 - largest factor of the number being reduced)
        
        if isPrime(i) and n % i == 0: # if this value is prime and the number is divisible by it
            
            primes.append(i) # add that prime factor to the list
            n /= i # divide out that prime factor from the number to start reducing the new number
            largestFactor /= i # divide out that prime factor from the largest factor to get the largest factor of the new number
            i = 2 # reset the prime factor test
        else:
            i += 1 # increment the factor test
            
    primes.append(int(n)) # add the last prime number that could not be factored
    primes.sort()
    return primes

def main():
    print (primeFactorization(1319587654321))
if __name__ == "__main__": main()
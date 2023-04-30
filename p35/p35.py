def check_prime(n):
    # determine if n is prime (True) or not (False)

    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            # n is not prime
            return False
        else:
            continue
    # cycled through all potential factors of n, none were found to divide n without a remainder, n is prime
    return True

def make_rotations(n):
    # returns a list with all rotations of digits in n
    n_str = str(n)

    results = []

    # the first result is n itself
    results.append(n_str)

    # now do the rotations
    for i in range(0, len(n_str) - 1):
        results.append(make_rotation(results[i]))

    # results is currently a list of strings, convert results to a list of ints
    for i in range(0, len(results)):
        results[i] = int(results[i])
    return results

def make_rotation(n):
    # rotates the digits in n a single spot
    result = []
    result.append(n[-1])
    for i in range(0, len(n)-1):
        result.append(n[i])
    return ''.join(result)

# set the limit, highest number to test

# want all circular primes below 1 million
limit = 999999

circular_primes = 0

for i in range(2, limit + 1):
    
    rotations = make_rotations(i)

    for j in range(0, len(rotations)):
        if check_prime(int(rotations[j])) == False:
            break
        if j == len(rotations)-1:
            print(rotations[j])
            circular_primes += 1

        
print(circular_primes)
# result is 55 circular primes below 1 million
# also tested with 13 circular primes below 100

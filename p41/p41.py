def check_prime(n):
    # if n is prime, return true, else return false

    # loop through prime numbers and check if n is divisible
    # if n is not divisible by all prime numbers up to n^0.5, then n is prime
    # else, n is divisible by at least 1 number other than 1 and is not prime
    #  
    for i in range(2,int(n**0.5)):

        # check if i (divides into n) is prime. if prime, then check if it divides into n
        if check_prime(i) is False:
            continue

        if n % i == 0:
            # n is not prime, i divides into n
            return False
        else:
            # we don't know if n is prime yet, continue checking
            continue

    return True

"""
321
231
213
132
123
"""
def make_permutation(n):
    # creates a list of all permutations, ordered largest to smallest, of numbers n through 1
    # ie. make_permutations(3) = [321, 231, 213, 132, 123]

    digits = range(n, 0, -1)
    print(digits)

    return digits

print(make_permutation(3)[1])

def swap(number, index1, index2):
    temp1 = number[index1]
    number[index1] = number[index2]
    number[index2] = temp1
    return number
"""
1 2 3 4 
1 2 4 3     23
1 3 2 4     13 23
1 3 4 2     23
1 4 2 3     12 23
1 4 3 2     23
2 1 3 4     
"""




def check_permutation(n):
    # checks if all digits in n are unique
    allowed_digits = range(1,len(str(n))+1)
    numbers = range(len(str(n)), 0, -1)

    for i in range(0, len(str(n))):
        # allowed checks if the digit in n is contained in the allowed digit list
        allowed = False

        for allowed_digit in allowed_digits:
            if str(n)[i] == str(allowed_digit):
                allowed = True
        if allowed == False:
            return False
        
        for j in range(i+1, len(str(n))):
            if str(n)[i] == str(n)[j]:
                return False
    return True




# print(check_permutation(7754321))



count = 0
guess = 987654321

while guess > 0:
    # print(guess)
    count += 1
    if count % 10 ** 6 == 0:
        print("Count: ",count)
        print("Guess: ", guess)
    
    if check_permutation(guess) == True:
        # all digits are unique
        if check_prime(guess) == True:
            # number is prime
            print(guess)
            break
    guess += -2

    # print(guess)

# solved with a bit of brute force (cycling and checking all descending odd numbers startins with 987654321) to get the correct answer 7652413
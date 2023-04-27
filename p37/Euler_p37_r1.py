# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:06:43 2018

Problem 92 from project euler.org

Worked on 
2018/09/25 (solves problem but the 11th number takes a long time to find)
    I verified my solution with https://www.rootnetsec.com/euler-truncatable-primes/
    to make sure the 11th prime was a large number that took a long time to find
    rather than an error in my program

@author: Jon
"""

def isprime(n):
    # returns true if n is prime
    if n == 1:
        # 1 is not prime
        return False
    
    if n == 2:
        # 2 is prime
        return True
    else:
        for i in range(2,n):
            if n%i == 0:
                # n is divisible by i
                return False
            elif i == n-1:
                # end of loop, no divisors found, n is prime
                return True
        
count = 0 # count the number of truncatable primes
res = 0 # store the sum
n = 10 # increment n to find truncatable primes

while count < 11:
    if isprime(n) == True:
    # check if n is prime
    
        for i in range(1,len(str(n))+1):
        # check if removing numbers from the right results in prime numbers
            if isprime(int(str(n)[0:i])) == False:
                break
            elif i == len(str(n)):
                for j in range(0,len(str(n))):
                # check if removing numbers from the left results in prime numbers
                    if isprime(int(str(n)[j:len(str(n))])) == False:
                        break
                    elif j == len(str(n))-1:
                        # n matches conditions, increment counter
                        count += 1
                        res += n
                        print(count)
                        print(n)

    n += 1
    
print(res)
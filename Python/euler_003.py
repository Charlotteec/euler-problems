#!/Usr/bin/env python

# 600851475143
factors = []

"""
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
"""


def isPrime(input):

    """
    Function to check if number is prime

    args:
    input(int): int to test for prime

    return:
    (bool): True if int is prime
    """

    for i in range(2, int(input/2)):
        if input % i == 0:
            return False
            break

    return True


def findFactors(input_var):

    """
    Fuction to find factors of a given number n

    args: input(int): to test if it is a factor

    return(array): the factors as an array
    """

    for i in range(2, int(input_var**(0.5))):
        if input_var % i == 0:
            factors.append(i)
            factors.append(input_var / i)

    return factors


def findPrimeFactors(factors_list):

    """
    Function to find prime factors

    args:
    factors_list(array): list of all factors-list

    return(null): no return; print instead
    print(int): print factors that are prime
    """
    prime_factors = []
    for x in factors_list:
        if isPrime(x):
            prime_factors.append(x)
    return prime_factors


factor_array = []       # array for factors
factor_array = findFactors(600851475143)
print(factor_array)     # call findFactors
print(max(findPrimeFactors(factor_array)))

# call findPrimeFactors on factor_array
# print(factor_array)     # print array of factorsct

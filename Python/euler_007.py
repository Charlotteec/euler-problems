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


def findPrime(end):
    i = 2
    prime_numbers = []
    while len(prime_numbers)<=end:
        if isPrime(i):
            prime_numbers.append(i)
            print(i)
        i += 1


prime_numbers = []
findPrime(10001)

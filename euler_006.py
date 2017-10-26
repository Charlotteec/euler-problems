

def sumOfSquares(num):
    squares = []
    for i in range(num+1):
        squares.append(i*i)
    return sum(squares)


def squareOfSums(num):
    numbers = []
    for i in range(num+1):
        numbers.append(i)
    nsum = sum(numbers)
    return nsum*nsum

print(sumOfSquares(100))
print(squareOfSums(100))

print(squareOfSums(100)-sumOfSquares(100))

#!/Usr/bin/env python

fiba = []
fib = 0
fib2 = 1
temp = 0

while temp < 4000000:
    temp = fib + fib2
    fib = fib2
    fib2 = temp
    print(fib)

    if temp % 2 == 0:
        fiba.append(temp)

print(fiba)
print(sum(fiba))


"""
function to check if a number (num) is divisible by every number in a range
with an iteration
"""


def isDivisible(num, min, max, iterate):
    x = 1
    for each in range(min, max, iterate):
        if num % each == 0:
            x += 1
        else:
            break
        if x == 20:
            return True


i = 0
evenlyDivisible = False
while evenlyDivisible is False:
    if isDivisible(i, 20, 1, -1) is True and i != 0:
        evenlyDivisible = True
    else:
        i += 20

print(i)

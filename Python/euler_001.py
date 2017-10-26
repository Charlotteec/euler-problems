#!/Usr/bin/env python


mult_three_or_five = []

for i in range(0, 1000):
    if i % 3 == 0:
        mult_three_or_five.append(i)
    elif i % 5 == 0:
        mult_three_or_five.append(i)
print(sum(mult_three_or_five))

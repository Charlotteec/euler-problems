#!usr/bin/env python


def isPalindrome(var):
    blah_str = str(var)
    if blah_str == blah_str[::-1]:
        return True


def find_product(min_int, max_int):
    p = []

    for num1 in range(min_int, (max_int)):
        for num2 in range(min_int, (max_int)):
            # random_var = num2 * num1
            if num2 <= num1:
                p.append(num1 * num2)

    return p


def main(min_int, max_int):

    var_2 = (find_product(min_int, max_int))
    p = []
    for each in var_2:
        if isPalindrome(each):
            p.append(each)
    print(max(p))

if __name__ == '__main__':
    main(100, 999)

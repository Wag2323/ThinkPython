import math


def compare(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1


def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    result = math.sqrt(dx**2 + dy**2)
    return result


def area(radius):
    return math.pi * radius**2


def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result


def circle_area2(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))


def is_divisible(x, y):
    return x % y == 0


def is_between(x, y, z):
    return x <= y and y <= z


def factorial(n):
    if not isinstance(n, int):
        print 'Factorial is only defined for integers.'
        return None
    elif n < 0:
        print 'Factorial is not defined for negative integers.'
        return None
    elif n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        return n * recurse


def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    elif m > 0 and n > 0:
        return ackermann(m-1, ackermann(m, n-1))
    else:
        print 'Values do not meet function requirements'
        return None


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) < 2:
        return 'Not long enough to be Palindrome'
    elif first(word) != last(word):
        return 'Not a Palindrome'
    else:
        inner = middle(word)
        if len(inner) < 2:
            return 'This is a Palindrome'
        else:
            return is_palindrome(inner)


if __name__ == '__main__':

    # x = 5
    # for y in range(0, 11):
        # c = compare(x, y)
        # print 'X is %g, Y is %g, Compare is %g' %(x, y, c)

    # print distance(10, 10, 5, 5)
    # print circle_area(10, 10, 5, 5)
    # print circle_area2(10, 10, 5, 5)

    # x = 5
    # z = 10
    # for y in range(1, 15):
        # b = is_between(x, y, z)
        # print 'Is %g between %g and %g? %g' %(y, x, z, b)

    # for x in range(0, 31, 3):
        # print "X is %d and it's Factorial is %d" %(x, factorial(x))
    # print factorial(1.5)
    # print factorial(-5)

    # print ackermann(3, 4)

    list = ['hello', 'wow', 'ww', 'am', 'www', 'test', 'redivider', '']
    for word in list:
        print word
        print is_palindrome(word)

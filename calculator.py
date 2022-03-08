from fractions import Fraction


def add(x, y):
    return x + y


def subs(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        print("ERROR can't divide by zero")
        return
    else:
        return x / y


def parsenum(a):
    alist = a.split('_')
    if len(alist) > 2:
        raise Exception("ERROR Invalid term: " + str(a))
        return
    if len(alist) > 1:
        temp = frac(alist[1])
        numerator = frac(alist[0]) + temp
        return Fraction(numerator)
    else:
        return frac(a)


def frac(a):
    alist = a.split('/')
    if len(alist) < 2:
        return Fraction(int(a))
    elif len(alist) > 1 & alist[1].isdigit():
        if alist[1] == 0:
            print("ERROR zero division")
            return
        return Fraction(int(alist[0]), int(alist[1]))
    else:
        print("ERROR Invalid term: " + str(a))
        return


def calculate(a, b, c):
    try:
        first = parsenum(a)
        second = parsenum(c)
    except:
        print("Error Invalid term: " + str(a) + str(c))
        return
    else:
        try:
            if b == '+':
                return add(first, second)
            elif b == '-':
                return subs(first, second)
            elif b == '*':
                return multiply(first, second)
            elif b == '/':
                return divide(first, second)
        except:
            print("Invalid operand: " + str(b))
            return


def printresult(a):
    if abs(a.numerator) > abs(a.denominator):
        whole = int(divide(a.numerator, a.denominator))
        numerator = int(a.numerator % a.denominator)
        if numerator == 0:
            print("=" + str(whole))
        else:
            print("=" + str(whole) + "_" + str(numerator) + "/" + str(a.denominator))
    else:
        print("=" + str(a))


def main():
    inputvalue = input("?")
    plist = inputvalue.split()

    try:
        result = calculate(plist.pop(0), plist.pop(0), plist.pop(0))
        printresult(result)
    except:
        print("Please enter a numeric term, operand, and numeric term")


main()

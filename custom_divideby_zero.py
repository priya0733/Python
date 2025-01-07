#Base class for other exceptions
class Error(Exception):
    pass

#raised when the input valuse is zero
class ZeroDivision(Exception):
    pass

try:
    Numerator = int(input("Enter a numerator: "))
    Denominator = int(input("Enter a denominator: "))
    if Denominator == 0:
        raise ZeroDivision
    else:
        print("success")
except ZeroDivision:
    print("Denominator is zero. DivisionByZeroExceptionError occurred!")
    print()
    
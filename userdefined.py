#define python user-defined exceptions

class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
number = 18

try:
    input_num=(int(input("Enter an Age: ")))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to vote")
        
except InvalidAgeException:
    print("Exception occured :Invalid Age")
    
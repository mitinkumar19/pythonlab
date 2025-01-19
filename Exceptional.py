a=int(input("enter first number: "))
b=int(input("Enter second number: "))
try:
    c=a/b   #raise zerodivisionerror
    print(c)
except Exception as e:
    print("Please enter correct value of denominator")
finally:
    print("finally b")
#-------------------------------------------------------------------------------------------------------------------------   
class exception:
    def __init__(self):
        a=int(input("enter first number: "))
        b=int(input("Enter second number: "))
        try:
            c=a/b   #raise zerodivisionerror
            print(c)
        except Exception as e:
            print("Please enter correct value of denominator")
        finally:
            print("finally b")
x=exception()
x.__init__
#-----------------------------------------------------------------------------------------------------------------------
class Error(Exception):
    """ base class for other exception"""
    pass
class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass
class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass
number =10
while True:
    try:
        i = int(input("Enter a number: "))
        if i < number:
            raise ValueTooSmallError
        elif i> number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
    except ValueTooLargeError:
        print("This value is too large, try again!")
print("congratulations!!! you guessed it correctly.")
                                  
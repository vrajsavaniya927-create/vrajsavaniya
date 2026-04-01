try:
    num1 = int(input("enter first num :"))
    num2 = int(input("enter second num :"))
    result = num1/num2
except ZeroDivisionError:
    print("you cannot divide any num by zero")
except ValueError:
    print("only int value are allowed")
else:
    print("division is =",result)
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ValueError:
    print("Invalid Number Entered")

except ZeroDivisionError:
    print("Cannot Divide by Zero")

except Exception as error:
    print("Unexpected Error:", error)
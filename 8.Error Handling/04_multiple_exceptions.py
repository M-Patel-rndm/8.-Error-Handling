try:
    num = int(input("Enter a number: "))

    result = 100 / num

    print("Result =", result)

except ValueError:
    print("Invalid Number")

except ZeroDivisionError:
    print("Cannot Divide by Zero")
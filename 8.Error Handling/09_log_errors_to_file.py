try:
    number = int(input("Enter a number: "))

    result = 100 / number

    print("Result =", result)

except Exception as error:

    file = open("error_log.txt", "a")

    file.write(str(error) + "\n")

    file.close()

    print("Error Logged Successfully")
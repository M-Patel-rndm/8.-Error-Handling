try:
    file = open("sample.txt", "r")

    print(file.read())

except FileNotFoundError:
    print("File Not Found")

finally:
    print("Program Finished")
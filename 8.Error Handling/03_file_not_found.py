try:
    file = open("sample.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:
    print("Error: File Not Found")
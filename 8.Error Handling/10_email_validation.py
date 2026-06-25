try:
    email = input("Enter Email: ")

    if "@" not in email or "." not in email:
        raise ValueError("Invalid Email Format")

    print("Valid Email")

except ValueError as error:
    print(error)
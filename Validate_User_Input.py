def validate_user_input():
    try:
        val = int(input("Enter an integer to proceed"))
        if type(val) == int:
            print("Thank you entering an int value")
    except ValueError:
        validate_user_input()


validate_user_input()
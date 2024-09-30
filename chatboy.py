"""
Get input from the user

Ensure that the input is a number
If the number is 1, add them
If the number is 2, subtract them
If the number is 3, multiple them
otherwise tell them invalid number

"""


def validate_int_input(user_response: str, user_input_message: str) -> int:
    while not user_response.isdigit():
        print(f"{user_response} is not a number")
        user_response: str = input(user_input_message)

    return user_response


print(
    "Hello. What would you like to do today?\n1. Add two numbers.\n2. Subtract two numbers\n3. Multiple two numbers"
)


user_input: str = input("> User: ")

user_input = validate_int_input(user_input, "\n> User: ")

if user_input == "1":
    first_number: str = input("Enter the first number\n> User: ")
    first_number = validate_int_input(first_number, "\n> User: ")

    second_number: str = input("Enter the second number\n> User: ")
    second_number = validate_int_input(
        second_number, "Enter the second number\n> User: "
    )

elif user_input == "2":
    first_number: str = input("Enter the first number")
    first_number = validate_int_input(first_number, "Enter the first number\n> User: ")

    second_number: str = input("Enter the second number")
    second_number = validate_int_input(
        second_number, "Enter the second number\n> User: "
    )


elif user_input == "3":
    first_number: str = input("Enter the first number")
    first_number = validate_int_input(first_number, "Enter the first number\n> User: ")

    second_number: str = input("Enter the second number")
    second_number = validate_int_input(
        second_number, "Enter the second number\n> User: "
    )

else:
    print(f"{user_input} is not a valid input option")

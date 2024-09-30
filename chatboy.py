"""
Get input from the user

Ensure that the input is a number
If the number is 1, add them
If the number is 2, subtract them
If the number is 3, multiple them
otherwise tell them invalid number

"""

user_prompt: str = "\n> User: "


def validate_int_input(user_response: str, user_input_message: str) -> int:
    while not user_response.isdigit():
        print(f"{user_response} is not a number")
        user_response: str = input(user_input_message)

    return user_response


print(
    "Hello. What would you like to do today?\n1. Add two numbers.\n2. Subtract two numbers\n3. Multiple two numbers"
)


user_input: str = input(user_prompt)

user_input = validate_int_input(user_input, f"{user_prompt} ")

if user_input == "1":
    first_number: str = input(f"Enter the first number{user_prompt} ")
    first_number = validate_int_input(first_number, f"{user_prompt}")

    second_number: str = input(f"Enter the second number{user_prompt} ")
    second_number = validate_int_input(
        second_number, f"Enter the second number{user_prompt} "
    )

elif user_input == "2":
    first_number: str = input(f"Enter the first number{user_prompt}")
    first_number = validate_int_input(
        first_number, f"Enter the first number{user_prompt} "
    )

    second_number: str = input(f"Enter the second number{user_prompt}")
    second_number = validate_int_input(
        second_number, f"Enter the second number{user_prompt} "
    )


elif user_input == "3":
    first_number: str = input(f"Enter the first number{user_prompt}")
    first_number = validate_int_input(
        first_number, f"Enter the first number{user_prompt} "
    )

    second_number: str = input(f"Enter the second number{user_prompt}")
    second_number = validate_int_input(
        second_number, f"Enter the second number{user_prompt} "
    )

else:
    print(f"{user_input} is not a valid input option")

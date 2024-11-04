import argparse


class CheckPassword:
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        "Validates all the requirements of the password"
        return (
            self.has_more_8_char()
            and self.has_capital()
            and self.has_lower_case()
            and self.has_number()
            and self.has_other_char()
        )

    def has_more_8_char(self, min_length=8):
        "Checks if the length of the password meets the requirements"
        return len(self.password) >= min_length

    def has_capital(self):
        "Checks if any of the characters in the password are upper case"
        return any(char.isupper() for char in self.password)

    def has_lower_case(self):
        "Checks if any of the characters in the password are lower case"
        return any(char.islower() for char in self.password)

    def has_number(self):
        "Checks if any of the characters in the password are digits (numbers)"
        return any(char.isdigit() for char in self.password)

    def has_other_char(self, other_char="_"):
        "Checks if the password contains other characters outside of the alphabet"
        return any(char in other_char for char in self.password)


def main():
    "Check the validity of a password parsed via the CLI"
    parser = argparse.ArgumentParser("Validate a password")
    parser.add_argument("password", type=str)
    args = parser.parse_args()

    password = args.password

    if CheckPassword(password).is_valid():
        print("Valid Password")
    else:
        print("Not Valid Password")


if __name__ == "__main__":
    main()

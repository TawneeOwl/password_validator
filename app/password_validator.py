import argparse

class CheckPassword:
    """
    This class defines the requirements for a password.

    Returns:
        boolean: True or false based on if all requirements
        are met when is_valid is called.
    """
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        "Validates all the requirements of the password"
        return (
            self.has_correct_length()
            and self.has_capital()
            and self.has_lower_case()
            and self.has_number()
            and self.has_specific_char()
        )

    def has_correct_length(self, min_length=8):
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

    def has_specific_char(self, specific_char="_"):
        "Checks if the password contains specific characters"
        return any(char in specific_char for char in self.password)


def main(password=None):
    """
    Check the validity of a password parsed.

    Args:
        password: Password data as a string.

    Returns:
        boolean: Returns True or False based on password validation
        str: Prints a string whether the password is valid or not
    """
    if password is None:
        parser = argparse.ArgumentParser("Validate a password")
        parser.add_argument("password", type=str)
        args = parser.parse_args()
        password = args.password

    if CheckPassword(password).is_valid():
        print("Valid Password")
        return True
    else:
        print("Not Valid Password")
        return False

if __name__ == "__main__":
    main()

from app.password_validator import CheckPassword

def test_valid_password():
    # Tests a valid password
    password = "Password123456_"
    assert CheckPassword(password).is_valid() == True

def test_password_length():
    # Test a short password
    password = "Pass12_"
    assert CheckPassword(password).is_valid() == False

    # Test minimum password length
    password = "Pass123_"
    assert CheckPassword(password).is_valid() == True

    # Test length change
    assert CheckPassword(password).has_correct_length(min_length = 10) == False

def test_password_case():
    # Test no lower case
    password = "PASSWORD123456_"
    assert CheckPassword(password).is_valid() == False

    # Test no upper case
    password = "password123456_"
    assert CheckPassword(password).is_valid() == False

def test_password_number():
    # Test no number
    password = "Password_"
    assert CheckPassword(password).is_valid() == False

def test_password_other_char():
    # Test no _ character
    password = "Password123456"
    assert CheckPassword(password).is_valid() == False
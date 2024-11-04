from app.password_validator import CheckPassword

def test_valid_password():
    # Tests a valid password
    password = "Password123456_"
    assert CheckPassword(password).is_valid() == True, "Expected pass for valid password"

def test_password_length():
    # Test a short password
    password = "Pass12_"
    assert CheckPassword(password).is_valid() == False, "Expected failure for password too short"

    # Test minimum password length
    password = "Pass123_"
    assert CheckPassword(password).is_valid() == True, "Expected pass for minimum password length"

    # Test length change
    assert CheckPassword(password).has_correct_length(min_length = 10) == False, "Expected failure for password below 10 character length"

def test_password_case():
    # Test no lower case
    password = "PASSWORD123456_"
    assert CheckPassword(password).is_valid() == False, "Expected failure for no lower case in password"

    # Test no upper case
    password = "password123456_"
    assert CheckPassword(password).is_valid() == False, "Expected failure for no upper case in password"

def test_password_number():
    # Test no number
    password = "Password_"
    assert CheckPassword(password).is_valid() == False, "Expected failure for no number in password"

def test_password_specific_char():
    # Test no _ character
    password = "Password123456"
    assert CheckPassword(password).is_valid() == False, "Expected failure for no '_' in password"

    # Test new character
    password = "Password12345?6"
    assert CheckPassword(password).has_specific_char(specific_char = "?") == True, "Expected pass with ? added to validator"
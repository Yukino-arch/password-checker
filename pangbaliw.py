import string

def check_password(password):
    condition_met = 0
    missing_requirements = []

    if len(password) >= 8:
        condition_met += 1
    else:
        missing_requirements.append("at least 8 character. ")

    if any(char.isupper() for char in password):
        condition_met += 1
    else:
        missing_requirements.append("atleast 1 uppercase letter. ")

    if any(char.islower() for char in password):
        condition_met += 1
    else:
        missing_requirements.append("atleast contain 1 lowercase letter. ")

    if any(char.isdigit() for char in password):
        condition_met += 1
    else:
        missing_requirements.append("atleast contain 1 number. ")

    special_character = '!@#$%^&*()_-+='
    if any(char in special_character for char in password):
        condition_met += 1
    else:
        missing_requirements.append("atleast contains 1 special character. ")


    if condition_met == 5:
        strength = "Strong"
    elif condition_met >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, missing_requirements
while True:
    password = input("Enter your password: ")
    strength,missing = check_password(password)

    print(f"Strength: {strength}")
    if strength != "Strong":
        print("Missing:", ", ".join(missing))



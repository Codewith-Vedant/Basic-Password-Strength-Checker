import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])

    if criteria_met == 5:
        strength = "Strong"
    elif criteria_met == 4:
        strength = "Moderate"
    elif criteria_met == 3:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = {
        "Length": "Met" if length_criteria else "Not Met",
        "Uppercase": "Met" if uppercase_criteria else "Not Met",
        "Lowercase": "Met" if lowercase_criteria else "Not Met",
        "Numbers": "Met" if number_criteria else "Not Met",
        "Special Characters": "Met" if special_criteria else "Not Met",
        "Strength": strength
    }

    return feedback

def main():
    print("Password Strength Assessment Tool")
    password = input("Enter your password: ")
    feedback = assess_password_strength(password)

    print("\nPassword Strength Assessment:")
    for criterion, status in feedback.items():
        print(f"{criterion}: {status}")

if __name__ == "__main__":
    main()

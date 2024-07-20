import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special_chars else ""

    all_characters = lowercase_letters + uppercase_letters + numbers + special_chars

    if not all_characters:
        raise ValueError("At least one character set must be enabled")

    password = "".join(random.choice(all_characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired length of the password: "))
    use_uppercase = input("Use uppercase letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Use numbers? (yes/no): ").lower() == "yes"
    use_special_chars = input("Use special characters? (yes/no): ").lower() == "yes"

    try:
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)
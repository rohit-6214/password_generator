import string
import random

def generate_password(length, complexity):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    if complexity == "weak":
        all_character = lower + digits
    elif complexity == "medium":
        all_character = upper + digits + lower
    elif complexity == "strong":
        all_character = upper + digits + lower + symbols
    else:
        raise ValueError("invalid choice")

    password = []
    if complexity == "medium":
        password.append(random.choice(upper))
        password.append(random.choice(digits))
        password.append(random.choice(lower))
    elif complexity == "strong":
        password.append(random.choice(upper))
        password.append(random.choice(digits))
        password.append(random.choice(lower))
        password.append(random.choice(symbols))

    password += random.choices(all_character, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)


print("welcome to password generator")

length = int(input("Enter the desired password length: "))
if length < 4:
    print("Password must be at least 4 characters long")
    exit()
else:
    complexity = input("Choose password complexity {'weak', 'medium', 'strong'}: ")

generated_password = generate_password(length, complexity)
print("Generated Password: ", generated_password)
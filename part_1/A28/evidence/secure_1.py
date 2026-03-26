import bcrypt

# Step 1: Check password strength
def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+[]{};:,.<>?/\\|" for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

# Step 2: Hash password with bcrypt
def hash_password(password):
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode("utf-8")

# Step 3: Store username and hashed password
def store_password(username, hashed_password):
    with open("passwords.txt", "a") as file:
        file.write(f"{username}:{hashed_password}\n")

# Main program
username = input("Enter username: ")
password = input("Enter password: ")

strength = check_password_strength(password)
print("Password strength:", strength)

if strength == "Weak":
    print("Password too weak. Try again.")
else:
    hashed = hash_password(password)
    store_password(username, hashed)
    print("Password stored securely.")
    print("Hashed password:", hashed)
username = input("Enter your username: ")
password = input("Enter your password: ")

print("========================================")
print("PASSWORD VALIDATION REPORT")
print("========================================")

print("Username:", username)
print("Password:", "*" * len(password))

print("--------- Validation Rules -------------")

if len(password) >= 8:
    print("[PASS] Minimum 8 characters (" + str(len(password)) + " characters)")
    rule1 = True
else:
    print("[FAIL] Minimum 8 characters")
    rule1 = False

has_digit = False
has_upper = False
for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True

if has_digit:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")
if has_upper:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")
print("------------ Result ------------------")

if rule1 and has_digit and has_upper:
    print("Password is VALID!")
    print("Account created successfully for", username + "!")
else:
    print("Password is INVALID.")

print("========================================")

# Email Slicer Program with Validation

# Get the email address from the user
email = input("Enter your email address: ").strip()

# Check if the email contains an '@' symbol
if '@' in email:
    # Split the email into two parts: username and domain
    username, domain = email.split('@')

    # Output the results
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email address. Please enter a valid email with '@'.")

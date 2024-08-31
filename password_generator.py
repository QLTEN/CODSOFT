import random
import string

def generate_password(length):
    # Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password (e.g., 8, 12, 16): "))
            if length < 4:
                print("Password length should be at least 4 characters for better security.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()

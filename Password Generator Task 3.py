# Importing the random module
import random
# Importing String module
import string

#Function that will generate a random password of length (n) and return it. 
def generate_password(n):
    
    # defining the characters to be used in making the password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(n))
    return password

def main():
    # Prompt user for password length
    try:
        password_length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Generate and display the password
    password = generate_password(password_length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

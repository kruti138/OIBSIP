import random
import string

def get_user_input():
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Length must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    if not (use_letters or use_numbers or use_symbols):
        print("You must select at least one character type.")
        return get_user_input()

    return length, use_letters, use_numbers,use_symbols
def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length, use_letters, use_numbers, use_symbols = get_user_input()
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
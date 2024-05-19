def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("Caesar Cipher")

    while True:
        text = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        text = encrypt(text, shift)
        print(f"Encrypted message: {text}")

        choice = input("Do you want to decrypt the message? (y/n): ").lower()

        if choice == 'y':
            text = decrypt(text, shift)
            print(f"Decrypted message: {text}")

        another_operation = input("Do you want to perform Caesar cipher on a new message? (y/n): ").lower()
        if another_operation != 'y':
            break


if __name__ == "__main__":
    main()

# Kayla Sahadeo's repository (encode() function)
def encode():
    password = input("Please enter your password to encode: ")
    encoded = []
    message = []
    for number in password:
        if 48 <= ord(number) <= 57:
            encoded.append((int(number)+3))
    for number in encoded:
        message.append(str(number))
    message = ''.join(message)
    print("Your password has been encoded and stored!")
    return message

if __name__ == "__main__":

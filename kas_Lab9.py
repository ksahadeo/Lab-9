# Kayla Sahadeo's repository (encode() function)
def encode(password):

    encoded = []
    message = []
    for number in password:
        if 48 <= ord(number) <= 57:
            encoded.append((int(number) + 3))
    for number in encoded:
        message.append(str(number))
    message = ''.join(message)
    print("Your password has been encoded and stored!")
    return message


def decode():
    pass


if __name__ == "__main__":
    use = True
    while use is True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        opt = input("Please enter an option: ")
        if opt == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
        elif opt == 2:
            decode()
        elif opt == 3:
            use = False

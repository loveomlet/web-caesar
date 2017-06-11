def rotate(letter, rot):
    if len(letter) != 1:
        return -1
    elif letter.isalpha() == False:
        return letter
    shift = 97 if letter.islower() else 65
    return chr((ord(letter) + rot - shift) % 26 + shift)

def encrypt(text, rot):
    message = ""
    for char in text:
        message += rotate(char, rot)
    return message

def main():
    text = input('Message: ')
    rot = int(input('Rotation: '))

    print(encrypt(text, rot))

if __name__ == "__main__":
    main()
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letter_len = len(letters)

def encrypt_decrypt_message():
    msg = str(input("Type Your message: "))
    shift_num = int(input("Type the shift number: "))
    return msg, shift_num


encrypt_message = ""
decrypt_message = ""
while True:
    encrypt_decrypt = input("Type 'encode' to encrypt , Type 'decode' to decrypt: ")
    if encrypt_decrypt == 'encode':
        message, shift = encrypt_decrypt_message()
        for messages in message:
            for letter in range(letter_len):
                if letters[letter] == messages:
                    encrypt_message += letters[int((letter + shift) % letter_len)]
        print(f"Here is your encode result: {encrypt_message}")
    else:
        message, shift = encrypt_decrypt_message()
        for message_decrypt in message:
            for letter in range(len(letters)):
                if letters[letter] == message_decrypt:
                    decrypt_message += letters[int((letter - shift) % letter_len)]
        print(f"Here is your decode result: {decrypt_message}")

    yes_no = input("Type 'Yes' if you want to go again. Otherwise type 'no' to close. ").lower()
    if yes_no == 'no':
        break




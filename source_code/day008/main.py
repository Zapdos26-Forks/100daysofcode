#from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            end_text += alphabet[(alphabet.index(char) + shift_amount) % 26]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


# enprint(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 25
    caesar(text, shift, direction)

    result = input(
        'Would you like to repeat the program again? "Yes" or "No"\n').lower()
    if result == "no":
        should_continue = False
        print("Goodbye")

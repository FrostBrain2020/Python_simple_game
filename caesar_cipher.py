def caesar(old_text, shift_amount, command):
    new_text = ""
    for letter in old_text:
        position = alphabet.index(letter)
        if command == "encode":
            new_position = (position + shift_amount) % 26
        elif command == "decode":
            new_position = (position - shift_amount) % 26
        else:
            print("I don't know what you want to do. Please try to provide correct values next time.")
            break
        new_text += alphabet[new_position]
    return new_text


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_program = "yes"
fin = False

while not fin:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(f"Here's the {direction}d result: {caesar(text, shift, direction)}")
    continue_program = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if continue_program == "yes":
        fin = True
        print("Goodbye")

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 
                   'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
                   'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 
                   'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', 
                   '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
                   }
# Function to encrypt the string according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            # Looks up the dictionary and adds the corresponding morse code along with a space to separate morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters and 2 indicates different words
            cipher += '  '
    return cipher

# Function to decrypt the string from morse to english
def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        # checks for space
        if letter != ' ':
            # storing morse code of a single character
            citext += letter
        else:
            # if i = 1 that indicates a new character
            if citext != '':
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
            decipher += ' '
    return decipher.strip()

# Hard-coded driver function to run the program
def main():
    while True:
        message = input("Enter the text you want to translate into morse code (or 'q' to quit): ")
        if message.lower() == 'q':
            break
        elif message.strip() == '':
            print("Please enter a valid message.")
            continue
        try:
            result = encrypt(message.upper())
            print(result)
        except KeyError:
            print("Invalid character in the message.")

        message = input("Enter the morse code you want to translate into text (or 'q' to quit): ")
        if message.lower() == 'q':
            break
        elif message.strip() == '':
            print("Please enter a valid morse code.")
            continue
        try:
            result = decrypt(message)
            print(result)
        except ValueError:
            print("Invalid morse code.")
if __name__  == "__main__":
    main()
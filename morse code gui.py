import tkinter as tk

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', " ":"/"}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != '':
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            cipher += ''
    return cipher

# Function to decrypt the string
# from morse to english
def decrypt(message):
    message += ' '
 
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            citext += letter
        else:
            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
            citext = ''
    return decipher

class MorseCodeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Morse Code Translator")

        self.text_to_morse_label = tk.Label(master, text="Text to Morse:")
        self.text_to_morse_label.pack()

        self.text_to_morse_entry = tk.Entry(master, width=50)
        self.text_to_morse_entry.pack()

        self.text_to_morse_button = tk.Button(master, text="Translate", command=self.text_to_morse)
        self.text_to_morse_button.pack()

        self.morse_to_text_label = tk.Label(master, text="Morse to Text:")
        self.morse_to_text_label.pack()

        self.morse_to_text_entry = tk.Entry(master, width=50)
        self.morse_to_text_entry.pack()

        self.morse_to_text_button = tk.Button(master, text="Translate", command=self.morse_to_text)
        self.morse_to_text_button.pack()

        self.result_label = tk.Label(master, text="Result:")
        self.result_label.pack()

        self.result_text = tk.Text(master, width=50, height=5)
        self.result_text.pack()

    def text_to_morse(self):
        message = self.text_to_morse_entry.get()
        result = encrypt(message.upper())
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def morse_to_text(self):
        message = self.morse_to_text_entry.get()
        result = decrypt(message)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

root = tk.Tk()
my_gui = MorseCodeGUI(root)
root.mainloop()
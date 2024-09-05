# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '&': '.-...', 
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', 
    '"': '.-..-.', '@': '.--.-', ' ': '/'
}

def text_to_morse_code(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('')
    return ' '.join(morse_code)

def morse_code_to_text(morse_code):
    inverse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    words = morse_code.split(' / ')
    decoded_message = []
    for word in words:
        chars = word.split(' ')
        decoded_word = []
        for char in chars:
            if char in inverse_dict:
                decoded_word.append(inverse_dict[char])
            else:
                decoded_word.append('')
        decoded_message.append(''.join(decoded_word))
    return ' '.join(decoded_message)

# main
text = "Hello World"
morse_code = text_to_morse_code(text)
print("Text to Morse Code:", morse_code)

decoded_text = morse_code_to_text(morse_code)
print("Morse Code to Text:", decoded_text)

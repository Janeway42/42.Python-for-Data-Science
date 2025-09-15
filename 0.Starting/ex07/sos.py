import argparse
import sys

# Morse code dictionary
MORSE_DICTIONARY = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',
    ' ': '/',
}

def translate_to_morse_code(text):
    encoded_text = []

    for char in text.upper():
        morse_character = MORSE_DICTIONARY.get(char, '')
        try:
            assert morse_character != '', "the arguments are bad"
            encoded_text.append(morse_character)
        except (ValueError, AssertionError) as e:
                print("AssertionError:", e)
                sys.exit(0)
    
    return ' '.join(encoded_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Script that scrapes images from a given website"
        )
    parser.add_argument("items", nargs="*", help="text to be analysed")
    args = parser.parse_args()

    try:
        assert len(args.items) == 1, "the arguments are bad"
        morse_text = translate_to_morse_code(args.items[0])
        print(morse_text)
    except (ValueError, AssertionError) as e:
            print("AssertionError:", e)
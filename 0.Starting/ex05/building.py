import argparse
import sys

def upercase(text):
    count = 0
    for char in text:
        if 'A' <= char <= 'Z':
            count += 1
    return count

def lowercase(text):
    count = 0
    for char in text:
        if 'a' <= char <= 'z':
            count += 1
    return count

def spaces(text):
    count = 0
    for char in text:
        if char == " " or char == "\n":
            count += 1
    return count

def punctuations(text):
    # Sentence endings: period, question mark, exclamation point
    # Comma, colon, and semicolon
    # Dash and hyphen
    # Brackets, braces, and parentheses
    # Apostrophe, quotation marks, and ellipsis
    punctuations = ".?!,:;-[]{}()'\"…"

    count = 0
    for char in text:
        if char in punctuations:
            count += 1
    return count

def digits(text):
    count = 0
    for char in text:
        if '0' <= char <= '9':
            count += 1
    return count
    
def main(input: str):
    print(f"The text contains {len(input)} characters")
    print(f"{upercase(input)} upper letters")
    print(f"{lowercase(input)} lower letters")
    print(f"{punctuations(input)} punctuation marks")
    print(f"{spaces(input)} spaces")
    print(f"{digits(input)} digits")


        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Script that scrapes images from a given website"
        )
    parser.add_argument("items", nargs="*", help="text to be analysed")
    args = parser.parse_args()

    if len(args.items) == 0:
        print("What is the text to count?")
        print("Type your input below and press Ctrl+D when done:")
        user_input = sys.stdin.read()
        if user_input:
            main(user_input)
        else:
            raise AssertionError("No input received from stdin.")
        
    else:
        try:
            assert len(args.items) == 1, "more than one argument is provided"
            main(args.items[0])
        except (ValueError, AssertionError) as e:
            print("AssertionError:", e)



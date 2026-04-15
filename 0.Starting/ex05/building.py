import argparse
import sys


def upercase(text):
    """Function upercase outputs the number of \
upercase characters in the string"""
    count = 0
    for char in text:
        if 'A' <= char <= 'Z':
            count += 1
    return count


def lowercase(text):
    """Function lowercase outputs the number of \
lowercase characters in the string"""
    count = 0
    for char in text:
        if 'a' <= char <= 'z':
            count += 1
    return count


def spaces(text):
    """Function spaces outputs the number of \
space chacaters in the string"""
    count = 0
    for char in text:
        if char == "\n" or char == " ":
            count += 1
    return count


def punctuations(text):
    """Function punctuations outputs the number of \
punctuation characters in the string"""
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
    """Function digits outputs the number of digits in the string"""
    count = 0
    for char in text:
        if '0' <= char <= '9':
            count += 1
    return count


def main(input: str):
    # print(upercase.__doc__)
    # print(lowercase.__doc__)
    # print(punctuations.__doc__)
    # print(spaces.__doc__)
    # print(digits.__doc__)
    print(f"\nThe text {input} contains {len(input)} characters")
    print(f"{upercase(input)} upper letters")
    print(f"{lowercase(input)} lower letters")
    print(f"{punctuations(input)} punctuation marks")
    print(f"{spaces(input)} spaces")
    print(f"{digits(input)} digits")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Script that analyses text"
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

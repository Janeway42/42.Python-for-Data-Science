from ft_filter import ft_filter
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Script that filters strings based on the length of the words"
        )
    parser.add_argument("items", nargs="*", help="text to be analysed and word size")
    args = parser.parse_args()

    try:
        assert len(args.items) == 2, "the arguments are bad"

        string = args.items[0]
        number = args.items[1]
        assert number.isdigit() == True, "the arguments are bad"
        number = int(number)

        if not all(char.isalpha() or char.isspace() for char in string):
            raise AssertionError("the arguments are bad")
        
        filtered = list(ft_filter(lambda word: len(word) > number, string.split()))

        print(f"{filtered}")

    except (ValueError, AssertionError) as e:
        print("AssertionError:", e)